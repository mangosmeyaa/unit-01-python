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
