# write a program to input a number and calculate the sum of digits of that number.
number = int(input("Enter a number: "))
sum_of_digits = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10

print("The sum of digits of", number, "is:", sum_of_digits)