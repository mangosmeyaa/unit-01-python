import datetime #<-- This module imports functions that work with dates and time. It shows different ways to display date and time other than as we know it

#Firstly, I created a variable and set it equal to the datetime. I use the now function and what it does is it grabs the date as well as the current time.
print()
print("Task 1")
my_now = datetime.datetime.now()
print("Current date and time:", my_now)
# Altogether, I printed the string to say what it is, and now it fetches the my_now variable that I created and combines it to show what the current date and time is.
print()
print("Task 2")

#This variable fetches the time and date again, so that it can change the format of it in US terms.
my_nowpt2 = datetime.datetime.now()
#What the strfttime function allows us to do is convert the date and time to a specific format. In this case we need it to have the slashes.
formats_date = my_nowpt2.strftime("%m/%d/%Y")
print("Current United States formatted date:", formats_date)
#This is going to print the current date in that new format.
print()
print("Task 3")
#Created two different variables that display two different dates. I made this so that it displays the difference in the days.
date_1 = "2025-11-25"
date_2 = "2025-12-25"
#This converts these strings into objects, specifically datetime objects. It treats it as actuallt something other than a number.
d1 = datetime.datetime.strptime(date_1, "%Y-%m-%d")
d2 = datetime.datetime.strptime(date_2, "%Y-%m-%d")

#We use the subtraction operator in order to determine the different
difference = d2 - d1

#Print the difference 
print("Difference in days is:", difference.days)
print()
print("Task 4")
#First variable will be to ask the user to put in their birthday essentially
birth_input = input("Enter your birthdate (MM/DD/YYYY): ")

#Change the input into an actual date using the strptime function.
birth_date = datetime.datetime.strptime(birth_input, "%m/%d/%Y").date()


#Todays date we need for this so we can find the different between the year now and the year the person was born
today = datetime.date.today()


#Take the age from this year and their birth year then prints the results which is your age.
age = today.year - birth_date.year
print("You are", age)
