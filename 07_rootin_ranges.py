# Exercise 1:
print()
print("Task 1")

# For loop is going to count numbers one through ten, except for 11 since it is exclusive.
for num in range(1, 11):
    print(num)

print()  # spacingg.


# Exercise 2:
print()
print("Task 2")

# Count by 10s from 900 to 1000, so we choose these numbers making sure 1,001 is exclusive so it stops at 1,000.
for value in range(900, 1001, 10):
    print(value)

print()  # some more spacing


# Exercise 3:
print()
print("Task 3")

# Count from 1 to 100 by 9s making sure to stop at 100.
for count in range(1, 101, 9):
    print(count)

print()  # more spacingg


print()
print("Task 4")
# Created a total variable to count the sum of all numbers from 1 to 10
total = 0
# Used range function in the "for" statement to loop through numbers from 1 to 10 and add them to the total variable
for x in range(1, 11):
    # Made sure to use the += operator to add the value of x to total so it adds up on each iteration.
    total += x
print("sum:", total)
print()


rows = 5

for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# The output shows a right-angled triangle made of stars sort of. Each row adds one more star than the previous row. The inner loop controls the amount of stars in each while the outer is controlling the  number of rows which is 5.