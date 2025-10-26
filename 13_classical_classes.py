"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

print("Task 1")
#Created a class called "Person", used the init method.
class Person:
    def __init__(self, name, age):
        self.name = name #Setting the attributes name and age in both lines.
        self.age = age
#This is the method to introduce the person.
    def introduce(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

#Created an object named wazih, and gave it an age of 17.
wazih = Person("Wazih", 17)

#Prints the name of the attribute of the object, name and age.
print(wazih.name)
print(wazih.age)

#This calls the introduce method to print out the entire introduction.
wazih.introduce()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print()
print("Task 2")
#Made the base class.
class Animal:
    speak = ''
    def __init__(self, name):
     self.name = name
     
#This is the first subclass "Dog".
class Dog: 
    speak = 'wolf'
   

    
     
#This are the variables just naming what is coming out of the speak method.
Meya1 = Animal("Dog: WOOF, WOOF!!" ) 
print(Meya1.name)

#Second subclass.
class Cat:
    speak = 'meow'
   

    
     
#Second variable just speaking what the cat will say. 
Meya2 = Animal("Cat: MEOWWWWWW!! :3 " )


print(Meya2.name)
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
print()
print("Task 3")
#Cretaed the bank account class with attributes self owner and balance.
class BankAccount:
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance

#Just made a function for my class using the self and amount for both depositing and withdrawing.
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount)
        
        else:
            print("Not enough balance sorry!")

#I created a variable called "account". 
account = BankAccount("Valerie", 65)

#These are the methods for testing the class. I included different amounts.
account.deposit(70) # <--First depositing $70.
account.withdraw(40)  #Then <-- Subtracting $30.
account.withdraw(100)# It is now trying to withdraw too much money.
