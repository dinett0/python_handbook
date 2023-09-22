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


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
