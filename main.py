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
    pass
