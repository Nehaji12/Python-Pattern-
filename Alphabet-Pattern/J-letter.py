def print_pattern_J(n) :
    for row in range(n): 
        for col in range(n): 
            if (row == 0 or col == n//2 or col == 0 and row > n//2 or row == n-1 and col < n//2 ): 
                print("*",end =  " ")
            else: 
                print(" ",end = " ") 
        print()
    print()



if __name__ == "__main__": 
    height_of_the_letter = int(input("Enter height of the letter \t ")) 
    print_pattern_J(height_of_the_letter)