#Task 1: I created a list of 4 items.
my_list = ["apple", "banana", "cherry", "date"]
print("Task 1:", my_list)
#Printed my elements to the console.

print("        ")

#Task 2: I added another item to the list.
my_list.append("elderberry")
print("Task 2:", my_list)
#Also, printed this to the console.

print("        ")

#Task 3: I am now removing an element from the list. I used the remove function in doing so.
my_list.remove("banana")
print("Task 3:" , my_list)
#Printed the results for the updated list.

print("        ")

#Task 4: I am now modifying or removing an item from the list and replacing with another fruit.
my_list[1] = "blueberry"  
print("Task 4:", my_list)
#Printed the results to show the changes.

print("        ")

#Task 5: I appended 3 more items to the list which just means adding 3 more things. But instead of using the append I used the extend method. Extending is when you add multiple items to a list at one time.
my_list.extend(["fig", "grape", "peach"])
print("Task 5:" , my_list)
#Printed to the console.

print("        ")

#Task 6: I am now going to delete a single element but at a specific index.
del my_list[0]
print("Task 6:", my_list)
#Printed to the console and deleted apple since it was the first item in the index.

print("        ")

#Task 7: Slicing something from the list. Created a new variable also.
first_two = my_list[:2]
print("Task 7:" , first_two)
#Printed to the console to account for the first two elements in the list. This made it so after it gets 2 it stops 0 and 1 are listed only.

print("        ")

#Task 8: Reusing the extend function from task 5. Same thing.
my_list.extend(["honeydew", "kiwi"])
print("Task 8:", my_list)
#Last time printing the results to console.







