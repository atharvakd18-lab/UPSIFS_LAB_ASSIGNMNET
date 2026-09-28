# write a program to check whether a given number is divisible by 3 and 6.
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 6 == 0:
    print(number, "is divisible by both 3 and 6.")
else:
    print(number, "is not divisible by both 3 and 6.")