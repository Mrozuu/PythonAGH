import random

numbers = []
n = 50
for i in range(n):
    numbers.append(random.randint(1, 100))

for i in range(n, 2, -1):
    for j in range(0, i-1, 1):
        if numbers[j] < numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)
