def print_patter_L(n): 
    for row in range(n): 
        for col in range(n): 
            if (col == 0 or row == n-1): 
                print("*",end =" ")
            else: 
                print(" ",end =" ")
        print() 
    print() 


if __name__ == "__main__": 
    height_of_the_letter =  int(input("Enter height of the letter \t "))
    print_patter_L(height_of_the_letter)