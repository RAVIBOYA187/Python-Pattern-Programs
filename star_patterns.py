def solid_square(n):
    for i in range(n):
        print("*" * n)


def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)


def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)


def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)


if __name__ == "__main__":
    n = int(input("Enter size: "))
    solid_square(n)
    print()
    right_triangle(n)
    print()
    inverted_right_triangle(n)
    print()
    pyramid(n)
    print()
    inverted_pyramid(n)
