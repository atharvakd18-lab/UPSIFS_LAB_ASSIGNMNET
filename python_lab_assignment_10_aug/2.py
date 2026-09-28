# . Write a Python function analyze_numbers(*args) that accepts any number of integers and displays the even numbers, odd numbers, sum of even numbers, sum of odd numbers, and their respective counts.
def analyze_numbers(*args):
    
    evens = [num for num in args if num % 2 == 0]
    odds = [num for num in args if num % 2 != 0]
    

    sum_evens = sum(evens)
    sum_odds = sum(odds)
    

    print("Even numbers:", evens)
    print("Odd numbers:", odds)
    print("Count of even numbers:", len(evens))
    print("Count of odd numbers:", len(odds))
    print("Sum of even numbers:", sum_evens)
    print("Sum of odd numbers:", sum_odds)

