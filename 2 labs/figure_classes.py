import math
# use abstact method ABC

class BasicFigure:
    name : str = "Basic Figure"

    def square(self):
        pass

class Rectangle(BasicFigure):
    name: str = "Rectangle"
    width: float = 1
    height: float = 1

    def __init__(self, width, height):
        self.width  = float(width)
        self.height = float(height)

    def square(self):
        return self.width * self.height

class Circle(BasicFigure):
    name    : str   = "Circle"
    radius  : float = 1

    def __init__(self, radius):
        self.radius = float(radius)

    def square(self) -> float:
        return math.pi * pow(self.radius, 2)

class Triangle(BasicFigure):
    name : str = "Triangle"
    firstSide   : float = 1
    secondSide  : float = 1
    thirdSide   : float = 1

    def __init__(self, firstSide, secondSide, thirdSide):
        self.firstSide = float(firstSide)
        self.secondSide = float(secondSide)
        self.thirdSide = float(thirdSide)

    def square(self):
        halfPerimetr = (self.firstSide + self.secondSide + self.thirdSide) / 2
        radical = halfPerimetr * (halfPerimetr - self.firstSide ) * \
                                 (halfPerimetr - self.secondSide) * \
                                 (halfPerimetr - self.thirdSide)

        return math.sqrt(radical)

if __name__ == "__main__":
    figure = Rectangle(10,20)
    print(figure.name)
    print(figure.square())
    figure = Circle(200)
    print(figure.name)
    print(figure.square())
    figure = Triangle(3,4,5)
    print(figure.name)
    print(figure.square())