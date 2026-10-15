
def print_pattern_C(n): 
    for i in range(n): 
        for j in range(n): 
            if (i == 0 or j == 0 or  i == n-1): 
                print("*", end = " ")
        print()
    print() 
    
            


if __name__== "__main__":
    height_of_the_letter = int(input("Enter height of the letter \t "))
    print_pattern_C(height_of_the_letter)