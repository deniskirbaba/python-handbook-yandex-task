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

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())

