import math

numbers = [number for number in range(16, 100, 4)]

full_squares = {i for i in numbers if i in [i**2 for i in range(1, max(numbers) + 1)]}

print(numbers)
print(full_squares)
