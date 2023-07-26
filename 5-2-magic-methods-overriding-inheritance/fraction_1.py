def gcd(a, b):
    while (r := a % b) != 0:
        a = b
        b = r
    return b


class Fraction():

    def __init__(self, num, denom=None):
        if isinstance(num, str):
            num, denom = map(int, num.split('/'))
        self.num, self.denom = num, denom
        self.__simplify__()

    def __str__(self):
        return f'{self.num}/{self.denom}'
    
    def __repr__(self):
        return f'Fraction({self.num}, {self.denom})'

    def __simplify__(self):
        d = gcd(self.num, self.denom)
        if d != 1:
            self.num, self.denom = int(self.num / d), int(self.denom / d)
    
    def numerator(self, number=None):
        if number is None:
            return self.num
        self.num = number
        self.__simplify__()

    def denominator(self, number=None):
        if number is None:
            return self.denom
        self.denom = number
        self.__simplify__()


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))
