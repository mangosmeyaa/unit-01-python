
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
user_input = input("Enter something: ")

if user_input == "":
    print("invalid")
else:
    print("valid")

#Task 3:
