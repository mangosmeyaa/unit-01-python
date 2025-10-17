#I created a contact list that is empty, so that whenever a user inpputs or deletes something in the contact book it is stored in this variable.
contactlist = {

}

#I used a while loop so that this statement keeps on going until the user inputs a number of choice.
while True:
    #In this part I created a dictionary for the book, set the values to 0, the keys the options.
    print()
    print("Contact Book Menu")
    book = {
        "1. Add Contact": 0,
        "2. Delete Contact": 0,
        "3. List Contacts": 0,
        "4. Exit": 0,
    }

    #Included a for statement to only be able to print out the options within the dictionary.
    for x in book:
        print(x)

    #I created my first input, which this prompts the user to enter one of the choices they want to do in this Contact Book.
    choice1 = input("Enter choice (TYPE THE NUMBER ONLY): ")
    #Choice 1:
    #Second input, asks the user if they want to add a contact.
    if choice1 == "1":
        print()
        name = input("Enter the name: ")
        phone = int(input("Enter the phone number: "))
        #Used a while statement, so that it keeps on going until the user decides on a actual valid phone number.
        while phone < 1000000000 or phone > 9999999999:
            print("Invalid phone number")
            phone = int(input("Enter the phone number: "))
        else:
            print("Contact added successfully!")
        #Contactlist will be stored using this format below, so that it displays that persons name and number.
        contactlist[name] = phone
    #Choice 2
    #Created the second input for the user to enter a name if they chose 2.
    elif choice1 == "2":
        print()
        choice3 = input("Enter the name: ")
        #Created a while statement so it will keep on going until the user inputs a valid name.
        while choice3 not in contactlist:
            print("Name not found")
            choice3 = input("Enter the name: ")
        else:
            print("Contact deleted successfully!")
            #Once valid, the name that is on the contact list will be deleted. I did this by using del function.
            del contactlist[choice3]
    #Choice 3.
    # If user goes for 3, they will get a list of all the contacts that are in the contact list.
    # Used a for statement NOT only get the name in the contact list but the number as well
    elif choice1 == "3":
        print()
        for name, phone in contactlist.items():
            print(f"{name}: {phone}")
    #CHoice 4.
    #I used the exit function to end the program if the user chooses number 4.
    elif choice1 == "4":
        exit()
    else:
        print("Invalid number")