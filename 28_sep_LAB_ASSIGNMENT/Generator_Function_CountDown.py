# Write  a generator function countdown(n) that yeilds numbers from n down to 1.
# use a loop to print the all numbers
 
def countdown(n):
    while n >= 1:
        yield n
        n = n - 1


n = int(input("Enter starting number: "))

print("Countdown:")
for num in countdown(n):
    print(num)