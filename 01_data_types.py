print("☆ Task 1 ")
print("-----------------")

#Firstly, I created my float variable. This variable is our tester.
my_float = 7.89

#Next, I made a variable equal to the integer and in the space I put the float variable inside.
my_int = int(my_float)

#Finally I printed the original float and the converted integer and printed this to the console. The console should show the conversion between the original float and the finale result it being a integer. The int function truncates the decimal part.
print(my_float)
print(my_int)

print("----------------")
print("☆ Task 2 ")

#User needs to put in a number any number.
number = float(input("Enter a number: "))
#If the number is greater than 0, it is deemed positive.
if number > 0:
    print("The number is positive.")
#If the number is less than 0, it is deemed negative.
elif number < 0:
    print("The number is negative.")
else:
    #If user puts 0, the number likely is 0.
    print("The number is zero.")

print("----------------")
print("☆ Task 3 ")

#User will just insert a random integer + float
int_num = int(input("Enter an integer: "))
float_num = float(input("Enter a float: "))
# Order of operations with the float and the integer.
print("Addition:", int_num + float_num)
print("Subtraction:", int_num - float_num)
print("Multiplication:", int_num * float_num)
#if and else statements just incase user uses 0 for any case scenario.
if float_num != 0:
    print("Division:", int_num / float_num)
else:
    print("Division: Cannot divide by zero")

print("----------------")
print("☆ Task 4 ")

#Creating a dictionary so that the fruits are there w the quanity of them. (values)
fruits = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}
#Next, printing this to the console so that the quanity of bananas using the "key" is listed
print("Quantity of bananas:", fruits["banana"])

print("----------------")
print("☆ Task 5 ")

#OG string with the comma that seperate the numbers
number_string = "1,2,3,4,5"
#Spilting the string into a list of strings
number_tuple = tuple(map(int, number_string.split(",")))
#Conversion of integers into tuple
#Print the results
print("Original string:", number_string)
print("Converted tuple:", number_tuple)

print("----------------")
print("☆ Task 6 ")

#Created my list of favorite subjects
subjects = ["Math", "Science", "History", "English"]
#Join methos to create the string w commas
joined_comma = ", ".join(subjects)
#Join again but with dashes
joined_dash = " - ".join(subjects)
#Print the results to the console.
print("Original list:", subjects)
print("Comma-separated string:", joined_comma)
print("Dash-separated string:", joined_dash)

print("----------------")

