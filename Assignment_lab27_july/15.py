# write a program that checks whether a given number is armstrong number or not.
number = int(input("Enter a number: "))
temp = number
sum_of_cubes = 0
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10
if sum_of_cubes == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
    