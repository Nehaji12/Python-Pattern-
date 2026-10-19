def print_pattern_V(n): 
    for row in range(n):
        for col in range(n): 
            if (col + row == n-1  or col == row ):
                if row <= n//2 :

                            
                    print("*",end = " ") 
                else: 
                    print(" ",end = " ")
            else: 
                print(" ",end = " ")
        print() 


if __name__ == "__main__": 
    height_of_the_letter = int(input("Enter height of the letter \t ")) 
    print_pattern_V(height_of_the_letter)
