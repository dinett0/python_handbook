class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = round(abs(a[0] - b[0]), 2)
        self.b = round(abs(a[1] - b[1]), 2)

    def perimeter(self):
        return round((self.a + self.b) * 2, 2)

    def area(self):
        return round(self.a * self.b, 2)


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
