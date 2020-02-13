from random import choice

class RandomWalk():
    def __init__(self, num_points=10000):
        self.num_points = num_points
        """Arraies, which stroes coordinations of points"""
        self.x_steps = [0]
        self.y_steps = [0]

    def get_step(self):
        direction = choice([0, 1, 2, 3, 4])
        distance = choice([-1, 1])
        step = direction * distance

        return step

    def make_steps(self):
        while len(self.x_steps) < self.num_points:
            step_x = self.get_step()
            step_y = self.get_step()

            if step_x == 0 and step_y == 0:
                continue

            next_x = self.x_steps[-1] + step_x
            next_y = self.y_steps[-1] + step_y

            self.x_steps.append(next_x)
            self.y_steps.append(next_y)
