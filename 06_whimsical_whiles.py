print ("Task 1")
#First, I created a variable and set it equal to one.
m = 1
#Then for any value of m that is less than 11 it's going to add 1 each time.
while m < 11:
   print(m)
   m += 1
#Printed my results to the console so that it adds one each time until it gets to 10. It stops counting after 9 and adds 1 to get to 10.

#This is printing the second task.
print ("            ")
print("Task 2")
print()

#Setting the variable equal to ten so that it knows to start from that number.
m = 10

#This shows that if m is greater than user it's going to count down.
while m > 0:
    print(m)
    m -= 1

print()

print("Task 3")
print()

# Ask the user for a number any.
number = int(input("Please give me a number: "))

# Start result at 1.
result = 1

# While the number is greater than 0, keep multiplying
while number > 0:
    result = result * number  # Multiply result by the current number
    number -= 1               # Subtract 1 each time

# Print the factorial result
print("The factorial is:", result)

# Bunch of spacing added.
print()
print("Task 4")
print()

# Setting variable to the right period, then asking for the user input to enter the password.
password = "mangos123"
user_input = input(" Please try to enter the password: ")

#While loop to determine if user entered the correct password. If they did it will say correct. If user did not enter correctly, they are stuck in an endless loop until guessed right.
while user_input != password:
    print("Nope, try again.")
    print()
    user_input = input("What's the password?")
else:
        print("It's correct, you are now logged in!")






