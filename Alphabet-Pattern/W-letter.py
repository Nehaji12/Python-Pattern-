def print_patteern_W(n): 
    for row in range(n): 
        for col in range(n): 
            if (col == 0 or col == n-1 or (col == row and row >= n//2) or (row +col == n-1 and row >=n // 2)):
                print("*",end = " ")
            else: 
                print(" ",end = " ")
        print()
    print() 


if __name__ == "__main__": 
    height_of_the_letter = int(input("Enter height of the letter \t")) 
    print_patteern_W(height_of_the_letter)