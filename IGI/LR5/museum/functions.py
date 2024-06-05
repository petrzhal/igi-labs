from datetime import datetime
from statistics import median, mean, mode
from django.db.models import Q, Avg, Max, Count, Sum, Prefetch, ExpressionWrapper, DecimalField, F
from django.db.models import FloatField
import matplotlib.pyplot as plt
import io
import base64
from urllib import parse
from collections import Counter

from matplotlib.colors import CSS4_COLORS

from museum.models import Order
from museum.models import Client, Exhibitions


def client_age_median():
    clients = Client.objects.filter(~Q(user__date_of_birth=None))
    ages = [(datetime.now().date() - client.user.date_of_birth).days // 365 for client in clients]
    if ages:
        return median(ages)
    else:
        return None


def client_age_mode():
    clients = Client.objects.filter(~Q(user__date_of_birth=None))
    ages = [(datetime.now().date() - client.user.date_of_birth).days // 365 for client in clients]
    if ages:
        return mean(ages)
    else:
        return None


def client_age_mean():
    clients = Client.objects.filter(~Q(user__date_of_birth=None))
    ages = [(datetime.now().date() - client.user.date_of_birth).days // 365 for client in clients]
    if ages:
        return mean(ages)
    else:
        return None


def get_order_with_highest_price():
    orders = Order.objects.all()

    if not orders:
        return None

    highest_price_order = max(orders, key=lambda x: x.get_total_price())
    return highest_price_order.get_total_price()


def get_most_popular_exhibition():
    orders = Order.objects.all()
    exhibition_counts = Counter(order.exhibitions.name for order in orders)
    most_common_word = exhibition_counts.most_common(1)[0][0]
    return most_common_word


def plot_halls():
    exhibition_counts = Exhibitions.objects.values('hall__name').annotate(total=Sum('people'))

    hall_names = [ec['hall__name'] for ec in exhibition_counts]
    visitor_counts = [ec['total'] for ec in exhibition_counts]

    light_green_color = CSS4_COLORS['lightgreen']

    plt.figure(figsize=(10, 6))
    plt.bar(hall_names, visitor_counts, color=light_green_color)
    plt.xlabel('Name of hall')
    plt.ylabel('Number of visitors')
    plt.title('Hall occupancy')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(visitor_counts):
        plt.text(i, count, str(count), ha='center', va='bottom')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = parse.quote(string)

    return url
