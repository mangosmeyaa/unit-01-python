#Task 1
print("Task 1")
print()
#Created a function called "greet" and defined it.
def greet(name):
    print("Hiii" , name + "!!")
#This print statement will greet their name, after they have inputted it.
users_name = input("What's your name?:) : ")
greet(users_name)
#This calls the greet function and passes the value stored in the variable above.
print()
#Task 2
print("Task 2")
#I will create a variable asking the user to pick a number. 
user_choice = int(input("What number do you pick? : "))
#I created a function and defined it num, using the return function so that number gets mulitpled.
def squaree(num):
    return num ** 2
# Print the product of the square, using the same variable that the user inputted.
print("The square is: ", squaree(user_choice))
print()
#Task 3
print("Task 3")
#Made a function and defined it.
def is_even(number_str):
    number = int(number_str) #Conversion of a string to integer
    return number % 2 == 0

#Asking the user to just input any number thats an integer.
num = int(input("Enter a number: "))

#Calling the function and printing the result of the number. 
if is_even(num):
    print(str(num) + " is even.")
else:
    print(str(num) + " is odd.")
print()
#Task 4
#I first created a  function that will be calcuting the area of a rectangle.
def rectangle_area(length, width):
    return length * width  #Using this return this will multiply both length and width to get the area (L*W).
#I will ask the user to input a length of a rectangle.
length = float(input("Enter the length of the rectangle: "))

#Do the same thing with the width ask them.
width = float(input("Enter the width of the rectangle: "))

#Im calling the function along with the user's input. This will print the area.
print("The area of the rectangle is " + str(rectangle_area(length, width)))
print()
#Task 5
print("Task 5")
def cel_to_fahren(celsius):
    return (celsius * 9 / 5) + 32 #This is the formula for converting fah to cel.

#Prompt the user to enter the temp in Celsius
celsius = float(input("Enter the temp in Celsius: "))

#I will call the function and it should print the conversion 
fahrenheit = cel_to_fahren(celsius)
print("The temperature in Fahrenheit is " + str(fahrenheit))
print()
#Task 6
print("Task 6")
#I define the function that will calculate the average list of all the numbers
def average(numbers):
    total = sum(numbers) #This is the total of all the numbers in the list
    count = len(numbers) #Then counting the numbers that are in the list
    return total / count #Final is to divide by total to get the average.
#First input so user inputs numbers. 
userr_input = input("Enter numbers with spaces in between: ")
#Then we take the string and make it into a list of numbers
numbers_list = [float(num) for num in userr_input.split()]  # Split input and convert each to float
avg = average(numbers_list)

# Print the average
print("The average of the numbers is " + str(avg))
print()
#Task 7
print("Task 7")
#First I defined the function to calculate the 3 things below.
def total_calculator(price, quantity, discount=0): #There was multiple ways to do this but I did it within the function. Setting all these 3 of values equal to 0. Im aware you can also create a variable outside the function too.
    total = price * quantity #You'd multiply the price w this to get the total.
    if discount > 0:
     total = total - (total * discount) #This applies the discount if given one.
     return total
#Asking the user for the price and quantity.
price = float(input("Enter the price: ")) #Simple conversions input to number.
quantity = int(input("Enter the quantity: "))  #Taking input to an integer.
#Ask user if there is a discount on the item.
discount_input = input("Enter discount as a decimal (or press enter if none): ")

#Conversion of discount if input is provided, if not 0
if discount_input == "":
    discount = 0
else:
    discount = float(discount_input)

#Calls the function with price, quantity, and discount.
total = total_calculator(price, quantity, discount)

#Prints the total altogether.
print("The total is " + str(total))


