# write a program to swap two number without using a temporary variables.

 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping using arithmetic
a = a + b   # Step 1
b = a - b   # Step 2
a = a - b   # Step 3

print(f"After swapping: a = {a}, b = {b}")
