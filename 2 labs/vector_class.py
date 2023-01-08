import math
class MyVector:
    x : float = 1
    y : float = 1

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def __eq__(self, other) -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return MyVector(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __mul__(self, other : float):
        return MyVector(self.x * other, self.y * other)

    def __imul__(self, other : float):
        self.x *= other
        self.y *= other
        return self
    
    def __str__(self) -> str:
        return ("<" + str(self.x) + ";" + str(self.y) + ">")

    def __repr__(self) -> str:
        return ("<" + str(self.x) + ";" + str(self.y) + ">")

    def scalarMul(self, other) -> float:
        return (self.x * other.y + self.y * other.y)
    
    def length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))
if __name__ == "__main__":
    firstVector = MyVector(3, 5)
    secondVector = MyVector(-4, 8)

    print(firstVector != secondVector)
    print(firstVector != firstVector) 
    print(firstVector + secondVector)

    print(firstVector - secondVector)
    print(secondVector - firstVector)

    firstVector -= secondVector
    print(firstVector)
    secondVector += firstVector
    print(secondVector)

    print(firstVector == secondVector)

    print(firstVector * -5)
    print(secondVector * 8)

    print(firstVector.scalarMul(secondVector))

    print(firstVector.length())
    print(secondVector.length())
