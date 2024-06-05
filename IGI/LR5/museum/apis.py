import requests


def get_random_gif():
    api_key = 'Eio5GQwmcuMOFpcd811Iu4fvlUBVjVDN'
    url = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}&rating=g'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['data']['images']['original']['url']
    except requests.exceptions.RequestException as e:
        print(f"Giphy API error: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing Giphy API response: {e}")
        return None


def get_cat_fact():
    url = 'https://catfact.ninja/fact'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['fact']
    except requests.exceptions.RequestException as e:
        print(f"Cat Facts API error: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing Cat Facts API response: {e}")
        return None
