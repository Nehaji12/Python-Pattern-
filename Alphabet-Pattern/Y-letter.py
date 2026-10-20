def print_pattern_Y(n) : 
    for row in range(n): 
        for col in range(n): 
            if (row == col and row <= n//2 or col + row == n-1 ):
                print("*",end = " ") 
            else: 
                print(" ",end = " ") 

        print()
    print() 

if __name__ == "__main__": 
    height_of_the_letter = int(input("Enter height of the letter \t")) 
    print_pattern_Y(height_of_the_letter) 
