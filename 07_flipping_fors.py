# Exercise 1:
# I created a variable with a cake flavor.
cakes = "Chocolate"

# This for loop prints each letter in the word "Chocolate"
for m in cakes:
    print(m)

print()  # spacingg.
 
# Exercise 2:
numbers = [2, 4, 6, 8, 10]  # A list of numbers
j = 0  # Start with 0 since we’re going to add each number to it.

# Using a for loop through each number in the list and add it to j.
for num in numbers:
    j += num

# This prints the total sum.
print("The sum of the list is:", j)

print()  # more spacinggg.


# Exercise 3:
sentence = "I love Full Stack Development"  # Just a quick random sentence.

# Split the sentence into a list of words.
words = sentence.split()

# This for loop is going through each word and print its length.
for word in words:
    print(word, "has length", len(word))

print()  # even more spacingg.


# Exercise 4:

# Created a dictionary with 4 key:value pairs
student = {
    "Name": "Meya",
    "Age": 16,
    "Grade": "11th",
    "Favorite Subject": "Computer Science"
}

for key, value in student.items():
    print(key, ":", value)

# I noticed that the order of the key:value pairs was not exactly what I expected.
# I thought they might print in the order I wrote them, but dictionaries don’t always guarantee that. But somehow it does?
