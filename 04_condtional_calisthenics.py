print("Task 1")

if 5 < 10:
   print("True")
else :
   print("False")

print("Task 2")
status=str(input("Are you under 18"))
if status == "yes":
    print("Ok the price is 10 dollars")
else:
    print("Ok then the price is 20")

print("Task 3")
my_fruits = ["strawberry", "raspberry", "blueberry", "peach"]
my_user = input("Enter a fruit name ")

if my_user in my_fruits:
    print("Yes, that fruit is in the list")
else:
    print("No, that fruit is not in the list.")

print("Task 5")
weight=int(input("What is the weight: "))#create variable for weight integer and zone string
zone=str(input("Which zone are you taking: "))
A=5#create varable for zone A and zone B
B=7

if weight <= 0:
    #First, I created the error if the weight weight is less than or equal to zero.
    print("Error")

if zone == "A" or zone == "zone A":#Second, I created if statements for Zone A as well as for Zone. These statements will do operations.
    weight * A
    print(weight * A)
elif zone == "B" or zone == "zone B":
    weight * B
    print(weight * B)
else:#I created the else statement just in the case that the user does not pick Zone A or Zone B.
    print("pick a zone")

