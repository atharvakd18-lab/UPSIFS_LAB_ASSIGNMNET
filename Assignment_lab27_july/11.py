# write a program to calculate volume of a cylinder using the formula V = π * r^2 * h
import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = math.pi * radius**2 * height
print("The volume of the cylinder is:", volume)