def welcome():
    print("Hello friend!")


def get_data():
    n = input("Напишите натуральное число: ")
    while not isinstance(n, int) or n < 1:
        n = input("Напишите натуральное число: ")
    return n


def goodbye():
    print("Goodbye!")


if __name__ == "__main__":
    pass
