import math
from .figure import geo_figure
from .color import fig_color

class circle(geo_figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = fig_color(color)

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "{} {} цвета радиусом {} имеет площадь {:.2f}".format(
            self.FIGURE_TYPE,
            self.color.color,
            self.radius,
            self.area()
        )
