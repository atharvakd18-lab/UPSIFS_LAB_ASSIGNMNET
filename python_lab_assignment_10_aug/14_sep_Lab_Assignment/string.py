# string manipulation 
# write a python program that accepts a string from the user and perform the following operations:
# 1. convert the string to uppercase
# 2. convert the string to lowercase
# 3. reverse the string
# 4. count the number of vowels in the string
  
# the program is as follows:
 
#  for program 1 :
  
# Program to convert a string to uppercase

user_input = input("Enter a string: ")

uppercase_string = user_input.upper()

print("Uppercase:", uppercase_string)

# for program 2:
 
  # Program to convert a string to lowercase

user_input = input("Enter a string: ")

lowercase_string = user_input.lower()

print("Lowercase:", lowercase_string)


# for program 3:
 
  # Program to reverse a string

user_input = input("Enter a string: ")

reversed_string = user_input[::-1]

print("Reversed:", reversed_string)

# for program 4:
 
  # Program to count vowels in a string

user_input = input("Enter a string: ")

vowel_count = 0

for char in user_input:
    if char in "aeiouAEIOU":
        vowel_count += 1

print("Number of vowels:", vowel_count)
