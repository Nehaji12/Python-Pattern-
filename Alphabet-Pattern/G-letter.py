def print_pattern_G(n): 
    for row in range(n) : 
        for col in range (n): 
            
            if (row == 0 or col == 0 or row == n-1 or col == n-1 and row >= n//2 or row == n//2 and col >= n//2):
                print("*",end= " ") 
            else : 
                print (" ",end = " ")
        print() 
    print() 



if __name__ == "__main__": 
    height_of_the_letter = int(input ("Enter height of the letter ")) 
    print_pattern_G(height_of_the_letter)