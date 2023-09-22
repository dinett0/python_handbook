class Rectangle:
    def __init__(self, a, b) -> None:
        self.static = (min(a[0], b[0]), max(a[1], b[1]))
        self.dynamic = (max(a[0], b[0]), min(a[1], b[1]))
        self.a = round(abs(a[0] - b[0]), 2)
        self.b = round(abs(a[1] - b[1]), 2)

    def round_point(self, point):
        return round(point[0], 2), round(point[1], 2)

    def perimeter(self):
        return round((self.a + self.b) * 2, 2)

    def area(self):
        return round(self.a * self.b, 2)

    def get_pos(self):
        return self.round_point(self.static)

    def get_size(self):
        return round(self.a, 2), round(self.b, 2)

    def move(self, dx, dy):
        self.static = (self.static[0] + dx, self.static[1] + dy)
        self.dynamic = (self.dynamic[0] + dx, self.dynamic[1] + dy)

    def resize(self, width, height):
        self.dynamic = (self.static[0] + width, self.static[1] + height)
        self.a = width
        self.b = height


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
