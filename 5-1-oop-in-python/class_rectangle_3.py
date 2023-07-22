class Rectangle():

    def __init__(self, p1, p2):
        self.p = (min([p1[0], p2[0]]), max([p1[1], p2[1]]))
        self.w = abs(max([p1[0], p2[0]]) - min([p1[0], p2[0]]))
        self.h = abs(max([p1[1], p2[1]]) - min([p1[1], p2[1]]))

    def perimeter(self):
        return round(2 * (self.w + self.h), 2)
    
    def area(self):
        return round(self.w * self.h, 2)
    
    def get_pos(self):
        return (round(self.p[0], 2), round(self.p[1], 2))
    
    def get_size(self):
        return (round(self.w, 2), round(self.h, 2))

    def move(self, dx, dy):
        self.p = (self.p[0] + dx, self.p[1] + dy)

    def resize(self, width, height):
        self.w = width
        self.h = height

    def center(self):
        return (round(self.p[0] + self.w / 2, 2), round(self.p[1] - self.h / 2, 2))

    def turn(self):
        c = self.center()
        self.w, self.h = self.h, self.w
        self.p = (c[0] - self.w / 2, c[1] + self.h / 2)

    def scale(self, factor):
        c = self.center()
        self.resize(round(self.w * factor, 2), round(self.h * factor, 2))
        res_c = self.center()
        self.move(c[0] - res_c[0], c[1] - res_c[1])


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')

