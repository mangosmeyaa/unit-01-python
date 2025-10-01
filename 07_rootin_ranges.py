"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

print()
print("TASK 1")

# Used range function in the "for" statement to print numbers from 1 to 10
for x in range(1, 11):
    print(x)
print()

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

print()
print("TASK 2")
# Used range function in the "for" statement to count by 10s from 900 to 1000 as 10 is the third part of the range function which is the step value
for x in range(900, 1001, 10):
    print(x)
print()


"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

print()
print("TASK 3")
# Used range function in the "for" statement to count by 9s from 1 to 100 as 9 is the third part of the range function which is the step value
for x in range(1, 101, 9):
    print(x)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

print()
print("TASK 4")
# Created a total variable to count the sum of all numbers from 1 to 10
total = 0
# Used range function in the "for" statement to loop through numbers from 1 to 10 and add them to the total variable
for x in range(1, 11):
    # Made sure to use the += operator to add the value of x to total so it adds up on each iteration.
    total += x
print("sum:", total)
print()

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5 
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()

# FIRST QUESTION:
# The output of the code is:
# *
# * *  
# * * *
# * * * *
# * * * * *

# SECOND QUESTION:
# The code displayed in the input shows the rows and tells how many rows there are.
# The for statement inside the other for statement then tells the number of stars as a string to be printed in each row.

