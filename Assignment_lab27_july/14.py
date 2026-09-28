# write a program that takes three digit from user and adds the square of each digit 
number = int(input("Enter a three-digit number: "))
sum_of_squares = 0
while number > 0:
    digit = number % 10
    sum_of_squares += digit ** 2
    number //= 10
print("The sum of squares of digits is:", sum_of_squares)
