def increasing_numbers(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def decreasing_numbers(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def continuous_numbers(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()


if __name__ == "__main__":
    n = int(input("Enter size: "))
    increasing_numbers(n)
    print()
    decreasing_numbers(n)
    print()
    continuous_numbers(n)
