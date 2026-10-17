def print_pattern_N(n): 
    for row in range(n): 
        for col in range(n): 
            if (col == 0 or col == n-1 or col == row ): 
                print("*",end = " ")
            else: 
                print(" ",end = " ")
        print() 
    print() 


if __name__ == "__main__": 
    height_of_the_letter  = int(input('Enter height of the letter \t '))
    print()
    print_pattern_N(height_of_the_letter)