# write a program that takes a string input 
# 1. print the first 3 character of the string 
# 2. Prints the last 2 character of the string
# 3. Prints the string with every second character 
# 4. Prints the string in reverse usingg slicing

#   the ccode iss as follows:
  
#    the program for 1 is:
 
user_input = input("Enter a string: ")
print("First 3 characters:", user_input[:3])

#    the program for 2 is:

user_input = input("Enter a string: ")
print("Last 2 characters:", user_input[-2:])

#    the program for 3 is:

user_input = input("Enter a string: ")
print("Every second character:", user_input[::2])

#    the program for 4 is:

user_input = input("Enter a string: ")
print("Reversed string:", user_input[::-1])