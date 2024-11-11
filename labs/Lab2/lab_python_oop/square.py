from .rectangle import rectangle

class square(rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side_length, color):
        super().__init__(side_length, side_length, color)

    def __repr__(self):
        return "{} {} цвета со стороной {} имеет площадь {:.2f}".format(
            self.FIGURE_TYPE,
            self.color,
            self.width,
            self.area()
        )
