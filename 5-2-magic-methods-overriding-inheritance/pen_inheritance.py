class Pencil:

    def __init__(self, color="blue"):
        self.color = color

    def draw_picture(self):
        return f"The picture is drawn in '{self.color}'."
    

class Pen(Pencil):

    def __init__(self, color, pen_type):
        super().__init__(color=color)
        self.pen_type = pen_type

    def sign_document(self):
        if self.color not in ("blue", "black", "purple"):
            return f"With pen in '{self.color}' can't sign the document."
        elif self.pen_type == 'gel':
            return f"With pen type '{self.pen_type}' can't sign the document."
        return f"Document signed."
    
    def draw_picture(self):
        return f"The picture is drwan with pen type '{self.pen_type}', color '{self.color}'."

    

blue_ball_pen = Pen(color="blue", pen_type="ball")
print(blue_ball_pen.draw_picture())
print(blue_ball_pen.sign_document())
blue_gel_pen = Pen(color="blue", pen_type="gel")
print(blue_gel_pen.draw_picture())
print(blue_gel_pen.sign_document())
