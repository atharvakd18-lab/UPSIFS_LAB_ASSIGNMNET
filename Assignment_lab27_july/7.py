# write a program to calulate the Euclidean distance between two points in 2D space.
import math

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

distance = math.hypot(x2 - x1, y2 - y1)
print("The Euclidean distance between the two points is:", distance)