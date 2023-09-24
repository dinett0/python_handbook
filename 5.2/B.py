class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_offset, y_offset):
        self.x += x_offset
        self.y += y_offset

    def length(self, relative_point):
        distance = (
            (self.x - relative_point.x) ** 2 + (self.y - relative_point.y) ** 2
        ) ** 0.5
        return round(distance, 2)


class PatchedPoint(Point):
    def __init__(self, x=None, y=None):
        if (not x) and (not y):
            x, y = 0, 0
        elif isinstance(x, tuple):
            x, y = x[0], x[1]
        else:
            x, y = x, y
        super().__init__(x, y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"PatchedPoint({self.x}, {self.y})"


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))
