# write a program to calculate simple interest using the formula SI = (P * R * T) / 100
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)
