"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print("Task 1")
#Created a class called "Person", used the init method 
class Person:
    def __init__ (self, name, age):
     self.name = name
     self.age = age

    def introduce(self):
        print(f"Hey, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Wazih", 17)

person1.introduce()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print()
print("Task 2")
# Task 2: Animals Speak

class Animal:
    def speak(self):
        pass  # empty method

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# test
dog1 = Dog()
cat1 = Cat()

dog1.speak()
cat1.speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
print()
print("Task 3")
class BankAccount:
    def __init__(self, owner):
       self.owner = owner
       self.balance = 0

def deposit(self,amount):
       self.balance = self.balance + amount
       print(self.owner + "deposited" + str(amount))


