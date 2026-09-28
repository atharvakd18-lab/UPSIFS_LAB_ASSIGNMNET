#  Create a decorator double_result that doubles the result of a function.
#  Apply it to a function add(a, b) that returns the sum of two numbers.




def double_result(func):
    def wrapper(a, b):
        result = func(a, b)
        return result * 2
    return wrapper


@double_result
def add(a, b):
    return a + b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Result =", add(a, b))