# write a program that takes a 4 digit number from the user and checks whether it is a narcissistic number or not.

num = int(input("Enter a 4-digit number: "))

original_num = num

sum_of_powers = 0

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** 4  
    num //= 10               
if sum_of_powers == original_num:
    print(f"{original_num} is a Narcissistic (Armstrong) number.")
else:
    print(f"{original_num} is NOT a Narcissistic number.")
