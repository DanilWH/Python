from random import choice

class RandomWalk():
    def __init__(self, num_steps=5000):
        self.num_steps = num_steps
        # walk begin by zero.
        self.x_steps = [0]
        self.y_steps = [0]
        self.z_steps = [0]

    def get_step(self):
        """Gets random step."""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def get_steps_walk(self):
        """Makes random step next."""
        while len(self.x_steps) < self.num_steps:
            step_x = self.get_step()
            step_y = self.get_step()
            step_z = self.get_step()

            if step_x == 0 and step_y == 0 and step_z == 0:
                continue

            next_x = self.x_steps[-1] + step_x
            next_y = self.y_steps[-1] + step_y
            next_z = self.z_steps[-1] + step_z

            self.x_steps.append(next_x)
            self.y_steps.append(next_y)
            self.z_steps.append(next_z)