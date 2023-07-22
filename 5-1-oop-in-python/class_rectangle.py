class Rectangle():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if p1[0] >= p2[0]:
            self.width = p1[0] - p2[0]
        else:
            self.width = p2[0] - p1[0]
        if p1[1] >= p2[1]:
            self.heigth = p1[1] - p2[1]
        else:
            self.heigth = p2[1] - p1[1]

    def perimeter(self):
        return round(2 * (self.width + self.heigth), 2)
    
    def area(self):
        return round(self.width * self.heigth, 2)
    

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

