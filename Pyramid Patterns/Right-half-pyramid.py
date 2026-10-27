def print_right_half(n): 
    for row in range(n): 
        for col in range(n): 
            if(col == row or  col<row ): 
                print("*" ,end =  " " ) 

            else: 
                print(" ",end = " ") 

        print() 
    print() 

if __name__ == "__main__": 
    height_of_the_pyramid = int(input("Enter height of the pyramid \t ") ) 


    print_right_half(height_of_the_pyramid)
