# write a python program using map() to find the cube of every number in number=[3,5,7,9]
number = [3, 5, 7, 9]
cubes = list(map(lambda x: x ** 3, number))
print(cubes)
