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

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])


first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
