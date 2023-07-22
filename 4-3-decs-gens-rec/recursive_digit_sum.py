def recursive_digit_sum(n):
    global res
    if 'res' not in globals():
        res = 0
    if n > 0:
        res += n % 10
        return recursive_digit_sum(n // 10)
    return res


result = recursive_digit_sum(7321346)
print(result)