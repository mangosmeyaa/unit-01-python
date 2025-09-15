
#Task 1:
 # I made a random password to act as the 'correct' password.
correct_password = "Apples123"

# User will then be instructed to type in their password
user_input = input("Enter your password: ")

# To check if the password matches
if user_input.upper() == correct_password.upper():
    print("Access granted.")
else:
    print("Access denied.")
    

#Task 2: 
#User is just asked to type something.

user_input = input("Enter something: ")
#If user types an empty string, it's marked as invalid
if user_input == "":
    print("invalid")
else:
    print("valid")
#If not, it's valid

#Task 3:

name= input("What's the best pet? Cat or Dog?:")
#So the user just needed to answer what they think their preference.
new_name = name.lower().replace("cat", "dog")
#Depending on what the user inputed it will automatically match with what they say.
print(new_name)
#Printing to the console.

#Task 4:
#The variables created, so that the user will input what their answers are.
name = input("Enter your name: ")
age = input("Enter your age: ")
#Printing results.
print("Name:", name)
print("Age:", age)


#Task 5:
#Inputs per usual.
num1 = float(input("Enter the first float: "))
num2 = float(input("Enter the second float: "))
#Statements determining what they input if they can round it to one place.
if num2 != 0:
    quotient = round(num1 / num2, 1)  # Round to 1 decimal place
    print("Quotient (rounded to 1 decimal):", quotient)
else:
    print("Cannot divide by zero.")
