import random

class PointDensity():
    def __init__(self, num_points=1000):
        self.num_points = num_points

        self.x_point = [0]
        self.y_point = [0]
        self.z_point = [0]

    def get_point(self):
        for lim in range(1, self.num_points):
            self.x_point.append(random.randint(-lim, lim))
            self.y_point.append(random.randint(-lim, lim))
            self.z_point.append(random.randint(-lim, lim))