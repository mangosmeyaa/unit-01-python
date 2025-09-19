print("Welcome to Meya's Calculatinator-inator 9000!!")
print()

num1 = float(input("Enter the first number: "))
print()
num2 = float(input("Enter the second number: "))

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")

choice= (input("Enter your choice: "))

if choice == "1":
        result = num1 + num2
        print(f"Result: {result}")
elif choice == "2":
        result = num1 - num2
        print(f"Result: {result}")
elif choice == "3":
        result = num1 * num2
        print(f"Result: {result}")
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Division by zero.")
elif choice == "5":
    if num2 != 0:
        result = num1 // num2
        print(f"Result: {result}")
    else:
        print("Error: Division by zero.")
elif choice == "6":
    result = num1 ** num2
    print(f"Result: {result}")
elif choice == "7":
    if num2 != 0:
        result = num1 % num2
        print(f"Result: {result}")
    else:
            print("Error: Modulo by zero.")
else:
    print("Invalid choice. Please select a number between 1 and 7.")


