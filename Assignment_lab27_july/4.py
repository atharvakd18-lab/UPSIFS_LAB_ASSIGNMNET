# write a program to reverse the digit of a given number
number = int(input("Enter a number: "))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = (reverse * 10) + digit
    number //= 10
print("The reverse of the number is:", reverse)
