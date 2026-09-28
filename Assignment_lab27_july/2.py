#  write a program to swap the values of three variables such that the first variables gets the value of the third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Swapping the values
a, b, c = c, a, b

print("After swapping:")
print("First number:", a)
print("Second number:", b)
print("Third number:", c)