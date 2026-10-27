def print_inverted_pyramid(n): 
    for row in range(n): 
        for col in range(n): 
            if (row == 0 or row > 0 and col < n-row):
                print("*",end =" ") 
            else: 
                print(" ",end = " ") 

        print() 
    print()

if __name__ == "__main__": 
    height_of_the_pyramid = int(input("Enter height of the pyramid \t ") ) 


    print_inverted_pyramid(height_of_the_pyramid)
