def gcd(a, b):
    while (r := a % b) != 0:
        a = b
        b = r
    return b


def lcm(a, b):
    return a * b / gcd(a, b)


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
    
    def __add__(self, other):
        res_denom = lcm(self.denom, other.denom)
        res_num = self.num * res_denom / self.denom + other.num * res_denom / other.denom
        return Fraction(int(res_num), int(res_denom))
    
    def __iadd__(self, other):
        res_denom = lcm(self.denom, other.denom)
        res_num = self.num * res_denom / self.denom + other.num * res_denom / other.denom
        self.num = int(res_num)
        self.denom = int(res_denom)
        self.__simplify__()
        return self
    
    def __sub__(self, other):
        res_denom = lcm(self.denom, other.denom)
        res_num = self.num * res_denom / self.denom - other.num * res_denom / other.denom
        return Fraction(int(res_num), int(res_denom))
    
    def __isub__(self, other):
        res_denom = lcm(self.denom, other.denom)
        res_num = self.num * res_denom / self.denom - other.num * res_denom / other.denom
        self.num = int(res_num)
        self.denom = int(res_denom)
        self.__simplify__()
        return self
    
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)
    
    def __imul__(self, other):
        self.num = self.num * other.num
        self.denom = self.denom * other.denom
        self.__simplify__()
        return self
    
    def __truediv__(self, other):
        return self * other.reverse()

    def __itruediv__(self, other):
        self.num = self.num * other.denom
        self.denom = self.denom * other.num
        self.__simplify__()
        return self
    
    def __lt__(self, other):
        return self.num / self.denom < other.num / other.denom
    
    def __gt__(self, other):
        return self.num / self.denom > other.num / other.denom
    
    def __le__(self, other):
        return self.num / self.denom <= other.num / other.denom
    
    def __ge__(self, other):
        return self.num / self.denom >= other.num / other.denom
    
    def __eq__(self, other):
        return self.num / self.denom == other.num / other.denom
    
    def __ne__(self, other):
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
    

a = Fraction(1, 3)
b = Fraction(6, 2).reverse()
print(a > b, a < b, a >= b, a <= b, a == b, a >= b)

