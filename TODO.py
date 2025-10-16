#Step 1: Create an empty list to store tasks
tasks = []

#Print a message to show the list is empty
print("Your task list is empty.")

#Start a while loop that will keep running forever and ever.
while True:
    # Ask the user what they want to do with their list. Do they want to add or remove something.
    action = input("Would you like to add or remove a task? ")

    # If the user wants to add a task, it will input the task they want to add to the list.
    if action == "add":
        # Ask what task to add
        task = input("Enter a task to add: ")
        # Add the task to the list
        tasks.append(task)
        # Show that it was added
        print("Added: " + task)

    #If the user wants to remove a task, it will input what task they'd like to remove. We would use elif so incase it's already empty it says nothing to remove.
    elif action == "remove":
        #This checks if the list is empty also.
        if tasks == []:
            print("Nothing to remove.")
        else:
            #Shows the list of tasks with numbers incase user thinks of removing it.
            count = 1
            for task in tasks:
                print(str(count) + ". " + task)
                count = count + 1

            #This asks the user which task number to remove, checks if it is in the list, and follows up with it being removed. I used the del function to achieve this.
            choice = input("Enter the task number to remove: ")
            #Check if input is a number.
            if choice.isdigit():
                number = int(choice)
                #Check if number is in the list range
                if number >= 1 and number <= len(tasks):
                     del tasks[number - 1]
                     print("Removed: " + removed)
                else:
                    print("That number is not on the list.")
            else:
                print("Please enter a valid number.")

    #If user adds something other than add or remove, I use another conditional to determine if 
    else:
        print("Type 'add' or 'remove'.")

    #Shows the updated list
    print("Current tasks:")
    #If the list is empty, it is.
    if tasks == []:
        print("List is empty.")
    #This shows all tasks.
    else:
        for t in tasks:
            print("- " + t)
    #Seperation I guess.
    print("-" * 30)
