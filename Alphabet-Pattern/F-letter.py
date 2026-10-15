def print_pattern_F(n): 
    for row in range(n): 
        for col in range(n): 
            if (row  == 0 or row == 3 or col == 0):
                print("*", end = " ")
        print()
    print()


if __name__ == "__main__": 
    height_of_the_letter = int(input("Enter height of the letter \t ")) 
    if height_of_the_letter < 5 : 
        print("you cant see exact picture of the F  letter so enter > 5 ")
    else: 
        print_pattern_F(height_of_the_letter)