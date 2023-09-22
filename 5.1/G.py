class Rectangle:
    def __init__(self, a, b) -> None:
        self.static = (min(a[0], b[0]), max(a[1], b[1]))
        self.a = round(abs(a[0] - b[0]), 2)
        self.b = round(abs(a[1] - b[1]), 2)

    def perimeter(self):
        return round((self.a + self.b) * 2, 2)

    def area(self):
        return round(self.a * self.b, 2)

    def get_pos(self):
        return round(self.static[0], 2), round(self.static[1], 2)

    def get_size(self):
        return round(self.a, 2), round(self.b, 2)

    def move(self, dx, dy):
        self.static = (self.static[0] + dx, self.static[1] + dy)

    def resize(self, width, height):
        self.a = width
        self.b = height

    def turn(self):
        self.a, self.b = self.b, self.a
        self.static = (-self.static[1], -self.static[0])

    def scale(self, factor):
        self.a *= 2
        self.b *= 2
        self.static = (self.static[0] * 2, self.static[0] * 2)


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep="\n")
rect.turn()
print(rect.get_pos(), rect.get_size(), sep="\n")
