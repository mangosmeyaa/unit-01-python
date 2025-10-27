print("Task 1: Division")
def divide_numbers(num1, num2):
    #It will try this operation.
    try:
        result = num1 / num2
        print("Result:", result)
    #If not successful, it says another message in result to the error. 
    except:
        print("Cannot divide by zero.")
# Example usage:
divide_numbers(10, 0)

print()

print("Task 2: Opening Files")

def read_file(filename):
    #It tries to loacate a file that doesn't exist in this.
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)

        file.close()
    #If it doesn't exist, (which likely doesn't), it prints a message saying that.
    except:
         print("File doesn't exist.")
# Example usage:
read_file("nonexistent.txt")

print()

print("Task 3: List Items")
def get_item(lst, index):
    #Trying this to see if that is on the list.
    try:
       item = lst[index]
       print("Item:", item)
    #Otherwise it doesn't, so again prints a message.
    except IndexError:
       print("This item doesn't exist in the list")
# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)

print()

print("Task 4: Dictionaries")

def get_value(dictionary, key):
    #Trying different values to see if there's one in the dictionary.
    try:
       value = dictionary[key]
       print("Value:", value)
       #There's not, so it prints that message.
    except KeyError:
     print("There is no key named c.")
# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")

print()

print("Task 5: Else/Finally")
def process_file(filename):
    #Trying this to see if it was found.
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("The file processes successfully.")
        #It was proccessed, so now the finally is basically like a confirmation message.
    finally:
        print("Execution is now complete.")
# Example usage:
process_file("example.txt")