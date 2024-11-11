from .figure import geo_figure
from .color import fig_color

class rectangle(geo_figure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} имеет площадь {:.2f}".format(
            self.FIGURE_TYPE,
            self.color,
            self.width,
            self.height,
            self.area()
        )