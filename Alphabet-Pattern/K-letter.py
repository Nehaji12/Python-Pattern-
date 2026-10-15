# def print_patter_K(n): 
#     for row in range(n) : 
#         for col in range(n): 
#             if (col == 0 and )



def print_pattern_K(n):
    mid = n // 2

    for row in range(n):
        for col in range(n):
            if (
                col == 0
                or col == mid - row
                or col == row - mid
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    height = int(input("Enter the height of the letter: "))
    print_pattern_K(height)
