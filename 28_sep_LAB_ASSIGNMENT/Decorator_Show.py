# write a decorator called show_info that printes:
# 1. 'callinng function..' before the function is run
# 2. 'function executed' after the function is run
#   Apply it to a fucnction square(num) that returns the square of a number 

def show_info(func):
    def wrapper(num):
        print("Calling function...")
        result = func(num)
        print("Function executed.")
        return result
    return wrapper


@show_info
def square(num):
    return num * num


n = int(input("Enter a number: "))
print("Square =", square(n))