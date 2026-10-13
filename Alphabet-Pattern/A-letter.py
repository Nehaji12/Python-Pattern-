''' 
1. Objective 
the goal of this programe is to print the capital letter A using Asterisk(*).
The programe visits each row and column , then decides whether to print a star or space 

2. Expectd output :
    *
   * *
  *****
 *     *
*       *

3. Understand the variable : 

n  ----> the height of the letter 
i  ----> the current row number. range(n) gives 0,1,2,3,4...etc..
j  -----> the current column number range(2*n-1).

4. How the nested loop work : 

The outer loop for i in range(n) , choose one row at a time. The inner loop, for j in range (2*n-1).
checks every column in that row. For each position, the if statment decides whether the character should be a 'star' or 'space'

print("*",end ="") print a star withour moving to a bnew line,
print(" ", end = "") prints a space without moving to a new line. 
After the inner loop finishes a arow , print() moves to the next line.

5. Explanation of the if condition : 

the conditions are connected by or. That means if any one of them is True , Python prints a star

    • (i == 0 and j == n - 1)
Prints the top point of A. When i is 0 and n is 5, j must be 4, the middle column.
    • j == n - 1 - i
Prints the left sloping side. As the row number i increases, the star column moves left.
    • j == n - 1 + i
Prints the right sloping side. As i increases, the star column moves right.
    • i == (n - 1) // 2 and n - 1 - i < j < n - 1 + i
Prints the inside of the middle bar on the middle row. For n = 5, i = 2, so the inequality becomes 2 < j < 6. Therefore j can be 3, 4, or 5. The two sloping-side conditions add stars at columns 2 and 6, making five stars across the middle row.


6. Useful Python concepts : 

    • Nested loops: a loop inside another loop.
    • range(n): generates numbers from 0 up to, but not including, n.
    • and: both connected conditions must be True.
    • or: at least one connected condition must be True.
    • Integer division (//): 5 // 2 gives 2.
    • Comparison operators: == checks equality; < means less than.

7. Understanding print_pattern() and entry point check: 

def print_pattern(): defines a function named print_pattern where it accepts Hight of the letter . The indented code belongs to that function and runs when print_pattern() is called.
if __name__ == "__main__":
Python sets __name__ to "__main__" when this file is run directly. The condition then calls print_pattern(). 

The quotation marks are important: "__main__" is a string. Writing print_patt() in the condition would try to call a function there and can cause a NameError if it has not been defined.
'''


def print_pattern(n): 

    for i in range(n): 

        for j in range(2 * n -1 ):

            if((i  == 0 and j == n -1)
                or (i >0 and j == n - 1 - i)
                or (i >0 and j == n - 1 + i)

                or (i == (n-1)//2 and n -1 -i < j < n -1 +i)): 
                print("*",end = " ")
            else:
                print(" ",end = " ")

        print()


if __name__ == "__main__":

    height_of_the_letter   = int(input("Enter Height of the letter   : \t"))
    print_pattern(height_of_the_letter)

