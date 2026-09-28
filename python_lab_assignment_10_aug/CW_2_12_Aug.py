# write a program using filter () and a lambda function to select no. greater than 50 from: number=[25,60,45,80,35,90]
number = [25, 60, 45, 80, 35, 90]
filtered_numbers = list(filter(lambda x: x > 50, number))
print(filtered_numbers)
