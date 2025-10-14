#Task 1
# This imports the random module. This will import the random
import random
print("Task 1")
print()
#This is going to be printing the fact that this dice will be rolled. The results are randomized. 
#For this specifically we need to use a for loop, so that it continues to generate random dice rolls each time it's asked.
#For the random method we will use the randrange. This returns a number that is in the range. Includes numbers from 1-10.
print("Rolling a six-sided dice 10 times")
print()
for roll in range(1,10):
    dice_result = random.randint(1,6) #Created this variable so we can reference in the print statement. We need a variable storing this randrange() method.
    print("Roll", roll + 1 ,":" ,dice_result, ) #Printed the results, included a colon so that it's spaced out


print("Task 2")
print()
#So for this, I am using the range function so that I can use a for loop to print numbers that are between 0 and one for the first segment.
print("Random numbers between the 0 and 1:")
for i in range(5):
    print(random.random())
#These two statements creates a for loop and the random function makes it return a float between 0 and 1. Range 5 just means it creates these numbers 5 times. Henceforth, why we need a for loop to achieve this (iterable).
print()
print("Random numbers that between 10 and 20:")
for i in range(5):
    print(random.uniform(10,20))
#For these lines of code. I created another for loop. So that 5 times it creates different numbers that are floats that are between the numbers 10 and 20. 

print("Task 3")
print()
#First, I will create a list of colors so it can select from this list. So I created this variable equal to a list.
colors_list = ["Teal", "Blue", "Beige", "Maroon", "Periwinkle" ]
#Then I will use another another method called the sample. The sample method in random module makes it so that it randomly picks out colors from the list. This means it picks without duplicates.
selected_colors = random.sample(colors_list,3) # <-- 3 just means it will select three colors from the list.
print("Randomly selected colors:", selected_colors)
# Prints the colors from the selected colors variable.

print("Task 4")
print()
#I created a variable and set it equal to a range between 1 and 10. So it goes from 1,11 stops at 10.
numbers_yk = list(range(1,11))
#The shuffle method in this module means it's going to rearrange the elements in place. This doesn't change original list.
random.shuffle(numbers_yk)
print("Shuffled list:", numbers_yk)
#Prints so that it prints the list but randomized and shuffled. No longer in order.