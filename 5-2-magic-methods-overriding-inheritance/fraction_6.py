def gcd(a, b):
    while (r := a % b) != 0:
        a = b
        b = r
    return b


def lcm(a, b):
    return a * b / gcd(a, b)


class Fraction():

    def __init__(self, num, denom=1):
        if isinstance(num, str):
            if '/' in num:
                num, denom = map(int, num.split('/'))
            else:
                num, denom = int(num), 1
        self.num, self.denom = num, denom
        self.__simplify__()

    def __str__(self):
        return f'{self.num}/{self.denom}'
    
    def __repr__(self):
        return f"Fraction('{self.num}/{self.denom}')"

    def __neg__(self):
        return Fraction(-self.num, self.denom)
    
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        res_denom = lcm(self.denom, other.denom)
        res_num = self.num * res_denom / self.denom + other.num * res_denom / other.denom
        return Fraction(int(res_num), int(res_denom))
    
    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        res_denom = lcm(self.denom, other.denom)
        res_num = self.num * res_denom / self.denom + other.num * res_denom / other.denom
        self.num = int(res_num)
        self.denom = int(res_denom)
        self.__simplify__()
        return self
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        res_denom = lcm(self.denom, other.denom)
        res_num = self.num * res_denom / self.denom - other.num * res_denom / other.denom
        return Fraction(int(res_num), int(res_denom))
    
    def __isub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        res_denom = lcm(self.denom, other.denom)
        res_num = self.num * res_denom / self.denom - other.num * res_denom / other.denom
        self.num = int(res_num)
        self.denom = int(res_denom)
        self.__simplify__()
        return self
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * other.num, self.denom * other.denom)
    
    def __imul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self.num = self.num * other.num
        self.denom = self.denom * other.denom
        self.__simplify__()
        return self
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self * other.reverse()

    def __itruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self.num = self.num * other.denom
        self.denom = self.denom * other.num
        self.__simplify__()
        return self
    
    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num / self.denom < other.num / other.denom
    
    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num / self.denom > other.num / other.denom
    
    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num / self.denom <= other.num / other.denom
    
    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num / self.denom >= other.num / other.denom
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num / self.denom == other.num / other.denom
    
    def __ne__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num / self.denom != other.num / other.denom

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

    def reverse(self):
        return Fraction(num=self.denom, denom=self.num)
    

a = Fraction(1, 2)
b = Fraction('2/3')
c, d = map(Fraction.reverse, (a + 2, b - 1))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)
