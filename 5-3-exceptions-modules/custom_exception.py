class NumbersError(Exception):
    pass


class EvenError(NumbersError):
    pass


class NegativeError(NumbersError):
    pass


def no_even(numbers):
    if all(x % 2 != 0 for x in numbers):
        return True
    else:
        raise EvenError('There must be no even numbers in the list.')
    

def no_negative(numbers):
    if all(x >= 0 for x in numbers):
        return True
    else:
        raise NegativeError('There must be no negative numbers in the list.')
    

def main():
    print('Enter the numbers on a single line separated by a space:')
    try:
        numbers = list(map(int, input().split()))
        if no_negative(numbers) and no_even(numbers):
            print(f'The sum of numbers: {sum(numbers)}.')
    except NumbersError as e:
        print(f'An error is ocurred: {e}')
    except Exception as e:
        print(f'An unforeseen error is ocurred: {e}')


if __name__ == '__main__':
    main()
