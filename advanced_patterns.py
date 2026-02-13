def diamond(n):
    # Upper part
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

    # Lower part
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    n = int(input("Enter size: "))
    diamond(n)
    print()
    hollow_square(n)
