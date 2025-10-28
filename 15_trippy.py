"""
Exercise 1: Divide
"""

def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b
assert divide(20,2) == 10 #Testing this function to see if this division operation work using the assert.
"""
Exercise 2: Factorial
"""

def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
assert factorial(4) #Testing to see if the factorial works properly. If it does, it should run.

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string
assert reverse_string("racecar")#Testing to see if reversed_string works, then using assert to verify.

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
assert fibonacci(6) + fibonacci(7)#I tested the fibonacci sequence to make sure it still works, then used assert to confirm.
"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,4})+"
  return re.match(email_regex, email) is not None
assert is_valid_email("mmiddleton2@brooklynsteamcenter.org") #Testing to make sure the @symbol is in the email, to validate the email address. 