from math_ import *


def welcome():
    print("Hello friend!")


def get_data():
    n = input("Напишите натуральное число: ")
    while not n.isdigit() or int(n) < 1:
        n = input("Напишите натуральное число: ")
    return int(n)


def goodbye():
    print("Goodbye!")


if __name__ == "__main__":
    welcome()
    n = get_data()
    fact = factorial(plus_plus(n))
    print(minus_minus(fact))
    goodbye()
