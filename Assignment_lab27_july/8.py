# write a program to check if three angles can form a valid triangle or not.
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("The three angles can form a valid triangle.")
else:
    print("The three angles cannot form a valid triangle.")