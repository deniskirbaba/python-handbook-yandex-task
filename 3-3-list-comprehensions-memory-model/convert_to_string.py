numbers = [int(i) for i in input().split()]

sorted_unique_string = ' - '.join([str(i) for i in sorted(list(set(numbers)))])

print(sorted_unique_string)
