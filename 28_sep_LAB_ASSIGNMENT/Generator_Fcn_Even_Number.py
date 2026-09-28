# Write a generator function even_numbers(limit) that yields  all even numbers up to the given limit.
#  use it to print even numbers up to 10.


def even_numbers(limit):
    for num in range(2, limit + 1, 2):
        yield num


n = int(input("Enter limit: "))

print("Even numbers:")
for num in even_numbers(n):
    print(num)