# Work №3
# Author: Zhalkovsky Petr
# Date: 01.04.2024
from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5

if __name__ == "__main__":
    while True:
        menu = int(input("Enter task number: "))
        match menu:
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                task4()
            case 5:
                task5()
