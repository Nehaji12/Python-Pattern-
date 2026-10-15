
def print_pattern_H(n):
    for row in range(n):
        for col in range(n):
            if col == 0 or row == n // 2 or col == n - 1:
                print("*", end=" ")
            else:

                #the space between two vertical lines 
                print(" ", end=" ")
        print()
    print()

if __name__ == "__main__":
    height_of_the_letter = int(input("Enter the height of the letter: "))
    print_pattern_H(height_of_the_letter)
