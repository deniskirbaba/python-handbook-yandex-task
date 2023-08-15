numbers = [int(i) for i in input().split()]

divisors = {number: [i for i in range(1, number // 2 + 1) if (number % i) == 0] + [number] for number in numbers}
print(divisors)
