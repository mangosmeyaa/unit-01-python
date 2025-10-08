import os
import sys

# First thing I was was create a variable set to the command. What the os.getcwd() does is that it checks to see which directory is running and checks for that.
print("Task 1")
print()
current_directory = os.getcwd()
print("Current working directory:", current_directory)
# It prints to the console showing what directory it is then it finds it within the console.

print()
print("Task 2")
print()
# I created a new folder, and used a another os command called makedirs. This command allows us to create new directories. I added the exist_ok because that is a boolean it checks to see if it exists. If it exists, it's "True".
os.makedirs('test_folder', exist_ok=True)

# List all files and directories in the current directory
items = os.listdir('.')

#This print the list, to display all the files/directory. Added a for loop so it says the condition everytime.
print("Files and directories in current directory:")
for item in items:
    print(item)



print()
print("Task 3")
print()

#I created a conditional, and used os.path to check if a given path point exists within my directory.
#If when it checks if data is a directory and its true, it returns that it exists already.
if os.path.isdir("data") == True:
    print("This directory already exists silly")
#I created an else statement because what if it doesn't exists? So it will say it doesn't exist. Then the user is asked to input that no and it automically creates it for u.
#This mkdir checks a specific directory to see if it's there.
#Prints this all to the console.   
else: 
    print("Wasn't even created. Directory doesn't exists.")
    creation = input("You want to create directory?")
    if creation == "Yes":
        os.mkdir("data")
        print("Directory created")

print()
print("Task 4")
print()

# We are using the os to get the current directory .
#Prints this and fetches it, then creating the conditional statement.
os.getcwd
print(os.getcwd())
os.listdir()
#This conditional looks for this directory, if it doesn't exists in it's path it prints an error message saying it can 't be found.
#If it was found within it's path it prints it was found.
if not os.path.exists("config.txt"):
    print("This file can't be found")
else:
    print("File was FOUNDD!!")


print()
print("Task 5")
print()

#Using the sys version command to print the version it's in. Simple. 
print(sys.version)

print()
print("Task 6")
print()

#This checks if it's friendly. If it's not it changes it back to a friendly name.
if sys.platform.lower() == "darwin":
    print("MacOS")