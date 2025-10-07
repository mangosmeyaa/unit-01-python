print("Problem 1")
print()

text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       count += 1

print(count)

print("Problem 2")
print()

print("give me a number")
n = int(input())  # convert input to integer

for num in range(1, n + 1):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")


print("Problem 3")
print()
if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num+1):
    result *= i   

  print("Factorial of " , num , "is" , result)

print("Problem 4")
print()

attempts = 0  # Setting the variable equal to 0 so that it starts counting after 0.

while True:
    password = input("Enter your password: ")

    if password == "secret":
        print("Correct password!")
        break
    else:
        attempts += 1
        print("Incorrect password")

    if attempts == 3:
        print("Too many attempts")
        break

    