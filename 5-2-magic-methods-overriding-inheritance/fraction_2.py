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
        return f"Fraction('{self.num}/{self.denom}')"

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def __simplify__(self):
        if self.num < 0 and self.denom < 0:
            self.num, self.denom = abs(self.num), abs(self.denom)
        elif self.num < 0 or self.denom < 0:
            self.num, self.denom = -abs(self.num), abs(self.denom)

        d = gcd(abs(self.num), self.denom)
        if d != 1:
            self.num, self.denom = int(self.num / d), int(self.denom / d)
    
    def numerator(self, number=None):
        if number is None:
            return abs(self.num)
        if self.num < 0:
            self.num = -number
        else:
            self.num = number
        self.__simplify__()

    def denominator(self, number=None):
        if number is None:
            return self.denom
        self.denom = number
        self.__simplify__()


a = Fraction(num=1, denom=1)
b = Fraction(num=1, denom=-1)
c = Fraction(num=-1, denom=1)
d = Fraction(num=-1, denom=-1)

print(a, b, c, d)
a.numerator(-1)
b.numerator(-1)
c.numerator(-1)
d.numerator(-1)
print(a, b, c, d)
a.denominator(-1)
b.denominator(-1)
c.denominator(-1)
d.denominator(-1)
print(a, b, c, d)
