class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, p):
        return round(((self.x - p.x)**2 + (self.y - p.y)**2)**0.5, 2)
    

class PatchedPoint(Point):

    def __init__(self, x=0, y=0):
        if isinstance(x, tuple):
            super().__init__(x[0], x[1])
        else:
            super().__init__(x, y)


point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)


