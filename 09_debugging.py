print("Solution #2")
#Two given variables: one that will act as a sentence and count the spaces, and another to start off the counter when it starts checking for the amount of spaces.
text = "Hello, world, my name is"
count = 0
#For loop, added a space inside of the quotation marks, so that Python knows it's not an empty string, it's still something (a space).
for char in text:
    if char == ' ':
        count += 1
#Printing the results which should count all the spaces in the text variable.
print(count)

print()
print("Solution #3")
n = int(input("Give me a number: ")) #In this line, I included int so that when it checks n it knows that it's a number. Since ranges don't read strings, they read numbers.
#For loop, and I added n+1 so it knows to go through the condition and include n at the end. It checks it's value and adds one until it gets to the final number.
for num in range(1, n + 1):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")
#Prints the numbers leading up until the final one, and should successfully determine if that number is even or odd.

print()
print("Solutions #4")
num = int(input("Enter an integer: "))
#Everything is right in the variable above
if num < 0: #<-- change this so that if it's less than 0, it knows negative ia a big no no.
    print("No negative numbers.")
else:
    result = 1
    for i in range(1, num + 1): #<-- included num in the range because we need it.
        result *= i
    print("Factorial of", num, "is", result)
  #Prints the final result which shows the factorial result of it, if everything beforehand went sucessfully.

print()
print("Solution #5")
#Seting the correct password to check against
correct_password = "secret"

#Start the counter.
attempts = 0

# Allow up to 3 attempts ONLY no more no less.
while attempts < 3:
    password = input("Enter your password: ")
    attempts += 1  #This adds the total attempts keeping track

    #This checks if the entered password matches the correct password
    if password == correct_password:  #This was previously comparing to wrong string.
        print("Correct password!")   # <-- success message should now show.
        break
    else:
        print("Incorrect password")    #Prints if password is wrong only.

#Check if user reached max attempts without success
if attempts >= 3:                  
    print("Too many attempts")
