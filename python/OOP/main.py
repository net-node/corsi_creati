class Point:

    points = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.points.append(self)

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    @classmethod
    def get_points(cls):
        return [str(p) for p in cls.points]

    @staticmethod
    def calc_distance(point1, point2):
        delta_x = abs(point1.x - point2.x)
        delta_y = abs(point1.y - point2.y)
        return (delta_x, delta_y)


p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(4, 2)

print(Point.get_points())
print(Point.calc_distance(p1, p3))
