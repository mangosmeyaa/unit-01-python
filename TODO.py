
# Created a list so anything can be added
# Step 1: Create an empty list
tasks = []

print("\nYour task list is empty.\n")

# Step 2: Start a loop to keep asking user what to do
while True:
    action = input("Would you like to add or remove a task? ").lower()

    # Step 3: Add a task
    if action == "add":
        task = input("Enter a task to add: ")
        tasks.append(task)
        print("Added: " + task)

    # Step 4: Remove a task
    elif action == "remove":
        if tasks == []:
            print("Nothing to remove.")
        else:
            # Show the list
            count = 1
            for task in tasks:
                print(str(count) + ". " + task)
                count = count + 1

            choice = input("Enter the task number to remove: ")
            if choice.isdigit():
                number = int(choice)
                if number >= 1 and number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print("Removed: " + removed)
                else:
                    print("That number is not on the list.")
            else:
                print("Please enter a valid number.")

    # Step 5: Handle invalid input
    else:
        print("Type 'add' or 'remove'.")

    # Step 6: Show updated list
    print("\nCurrent tasks:")
    if tasks == []:
        print("List is empty.")
    else:
        for t in tasks:
            print("- " + t)
    print("-" * 30)