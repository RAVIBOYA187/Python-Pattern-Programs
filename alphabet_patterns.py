def increasing_alphabet(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()


def same_alphabet_row(n):
    for i in range(n):
        print(chr(65 + i) * n)


def alphabet_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()


if __name__ == "__main__":
    n = int(input("Enter size: "))
    increasing_alphabet(n)
    print()
    same_alphabet_row(n)
    print()
    alphabet_triangle(n)
