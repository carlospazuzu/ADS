import math 

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

    def get_quadrant(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4

    def move(self, x, y):
        self.x += x
        self.y += y

