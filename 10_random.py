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



