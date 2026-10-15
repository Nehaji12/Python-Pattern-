def print_pattern_E(n): 
        
    for row in range(n): 
        for col in range(n): 
            if (row == 0 or row == n//2 or row == n-1 or col == 0): 
                print("*",end = " ")
        print()
    print()

if __name__ == "__main__": 
    height_of_the_letter =  int(input("Enter height of the letter \t ")) 
    print_pattern_E(height_of_the_letter)