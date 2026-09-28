# take 10 integer from user, store in a list ,then find sum and average without using sum()
import numbers

numbers = []

for _ in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)

total = 0
for n in numbers:
    total += n

average = total / len(numbers) if numbers else 0
print("Sum:", total)
print("Average:", average)