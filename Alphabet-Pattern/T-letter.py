def print_patter_T(n): 
    for row in  range(n) : 
        for col in range (n): 
            if (row == 0 or col == n//2): 
                print("*",end = " ") 
            else: 
                print(" ",end = " ")
        print()

    print()

if __name__  == "__main__": 
    height_of_the_letter = int(input ("Enter height of the letter  \t "))
    print_patter_T(height_of_the_letter)