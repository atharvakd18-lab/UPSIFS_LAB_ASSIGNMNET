#  write a program using reduce() and a lambda function to find the sum of all the number , number=[5,10,15,20]

from functools import reduce


number = [5, 10, 15, 20]
total = reduce(lambda x, y: x + y, number)
print(total)
