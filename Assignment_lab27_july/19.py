# write a program to swap two numbers using a temporary variables.


 # Program to swap two numbers using a temporary variable

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")
