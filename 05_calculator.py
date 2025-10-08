# This prints a welcome message to my calculator.
print("Welcome to Meya's Calculatinator-inator 9000!!")

print()  # --> Just some extra spacing in between, so the statements are better spaced.


# This code asks the user for two numbers and saves them as variables for the console. This is referenced for the operators we will use for this calculator. Then converting it to a float for both variables.
# Try to get two numbers from the user. If it's a letter, I made sure it returns as such. Try function in python tries a block of the code then if there's a value where it doesn't recgonize it as a number, stead as a letter it should give an error.
try:
    num1 = float(input("Enter the first number: "))
    print()
    num2 = float(input("Enter the second number: "))
except ValueError:
    # If the user types a letter instead of a number
    print("Please enter numbers only!")
    exit()  # stops the program from progressing since invalid.

# I just created a list of operations to choose from, then printed them to the console. This allows the user to choose the operation for the numbers they selected.
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")

# User's choice for which operation they want to do.
choice = (input("Enter your choice: "))

# Based on input, we write 7 different conditional statements based on the situation. As listed below.

# If the user picked "1", add the two numbers (variables) num 1 + num 2.
if choice == "1":
    result = num1 + num2
    print(f"Result: {result}")  # shows the results.

# If the user picked "2", subtract num 1 - num 2.
elif choice == "2":
    result = num1 - num2
    print(f"Result: {result}")

# If the user picked "3", multiply the two numbers (both variables).
elif choice == "3":
    result = num1 * num2
    print(f"Result: {result}")

# If the user picked "4", divide the first number by the second (both variables).
elif choice == "4":
    if num2 != 0:  # Makes sure we’re not dividing by zero.
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Division by zero.")  #This shows an error if dividing by zero.

# If the user picked "5", do floor division (gives the whole number result from both variables).
elif choice == "5":
    if num2 != 0:  # Checks again to avoid dividing by zero
        result = num1 // num2
        print(f"Result: {result}")
    else:
        print("Error: Division by zero.")

# If the user picked "6", raise the first number to the power of the second.
elif choice == "6":
    result = num1 ** num2
    print(f"Result: {result}")

# If the user picked "7", find the remainder when the first number is divided by the second.
elif choice == "7":
    if num2 != 0:  # Checks to make sure we’re not dividing by zero
        result = num1 % num2
        print(f"Result: {result}")
    else:
        print("Error: Modulo by zero.")

# If the user didn’t pick a valid option.
else:
    print("Invalid choice. Please select a number between 1 and 7.")


