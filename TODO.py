my_todo = []

print()
print("Nothing on your list!!")
print()
while True:
    my_list = input("Would u want to either remove or add something? ")
    if my_list == "add":
        my_list.append(input("What would you like to add to the list?"))
    elif my_list == "remove":
        my_list.remove(input("What number would you like to remove the list?"))
        my_list -= 1
    else:
        print("Invalid")
        print()
    print()
    for x in my_list:
        print(x)
    print()





    why