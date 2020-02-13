from random import choice

class RandomWalk3D():
    def __init__(self, num_points=1000):
        self.num_points = num_points

        self.x_steps = [0]
        self.y_steps = [0]
        self.z_steps = [0]

    def get_step(self):
        distance = choice([0, 1, 2, 3, 4])
        declaration = choice([-1, 1])
        step = declaration * distance

        return step

    def random_steps(self):
        while len(self.x_steps) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            z_step = self.get_step()

            if x_step == 0 and y_step == 0 and z_step == 0:
                continue

            next_x = self.x_steps[-1] + x_step
            next_y = self.y_steps[-1] + y_step
            next_z = self.z_steps[-1] + z_step

            self.x_steps.append(next_x)
            self.y_steps.append(next_y)
            self.z_steps.append(next_z)
