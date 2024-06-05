from Task1.task1 import Task1
from Task2.task2 import Mixer
from Task3.task3 import Task3
from Task4.task4 import Task4
from Task5.task5 import Task5

if __name__ == '__main__':
    while True:
        choise = int(input("Enter number of task: "))
        match choise:
            case 1:
                Task1().start()
            case 2:
                Mixer('/home/petr/PycharmProjects/igi_lr4/Task2/input.txt').start()
            case 3:
                Task3().start()
            case 4:
                Task4().start()
            case 5:
                Task5().start()
