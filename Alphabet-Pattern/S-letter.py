
def print_pattern_S(n):
    for row in range(n):
        for col in range(n):
            if (
                row == 0
                or (col == 0 and row <= n // 2)
                or row == n // 2
                or (col == n - 1 and row >= n // 2)
                or row == n - 1
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the height of the letter: \t"))
    print_pattern_S(n)
