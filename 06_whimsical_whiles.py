#TASK 1
print ("Task 1")
#First, I created a variable and set it equal to one.
m = 1
#Then for any value of m that is less than 11 it's going to add 1 each time.
while m < 11:
   print(m)
   m += 1
#Printed my results to the console so that it adds one each time until it gets to 10. It stops counting after 9 and adds 1 to get to 10.
print ("            ")


m = 10

print("       ")
while m > 0:
    print(m)
    m -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
number =  int(input("give me number now pls"))
result = 1

while number > 0:
      
      result = number * result
      number -= 1
      
print(result)


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = "mangos123"
user_input = input("Please try to enter the password")

while user_input != password:
    print("its wrong")
    user_input = input("whats it")
else:
        print("correct")






