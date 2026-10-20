def print_patter_P(n): 
    for row in range(n): 
        for col in range(n): 
            if (col == 0 or row == 0 and col < n -1  or row == n//2 and col < n-1 or col == n -1 and row > 0  and row < n//2  ):
                print("*",end = " ")
            else: 
                print(" ",end = " ")
        print()

    print()


if __name__ == "__main__": 
    height_of_the_letter = int(input("Enter height of the letter \t "))
    print_patter_P(height_of_the_letter)     
