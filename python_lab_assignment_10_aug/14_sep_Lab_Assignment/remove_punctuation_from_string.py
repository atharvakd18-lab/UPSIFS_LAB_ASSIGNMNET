#  write a python program to remove all punctuation from a given string, using string methods or the string module

import string

user_input = input("Enter a string: ")
cleaned_string = user_input.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", cleaned_string)

