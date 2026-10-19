def print_pattern_X(n): 
    for row in range(n):
        for col in range(n): 
            if (row == col or col ==  n -1- row): 
                print("*",end = " ") 
            else: 
                print(" ",end = " ") 
        print()
    print() 


if __name__ == "__main__": 
    height_of_the_letter = int(input("Enter height of the letter \t ")) 
    print_pattern_X(height_of_the_letter)
