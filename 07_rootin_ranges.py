
# Exercise 1:

print()
print("Task 1")

# I used the range function in the "for" statement to print numbers from 1 to 10.
for x in range(1, 11):
    print(x)
print()

# Exercise 2:
print()
print("Task 2")
# Used range function in the "for" statement to count by 10s from 900 to 1000 as 10 is the third part of the range function which is the step value
for x in range(900, 1001, 10):
    print(x)
print()

# Exercise 3:

print()
print("Task 3")
# Used range function in the "for" statement to count by 9s from 1 to 100 as 9 is the third part of the range function which is the step value
for x in range(1, 101, 9):
    print(x)

# Exercise 4:

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

# Excercise 5:


rows = 5 
for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()


