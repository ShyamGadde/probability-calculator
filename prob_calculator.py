import random
import copy
from collections import Counter


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents += [color] * count

    def draw(self, times):
        output = []
        if times >= len(self.contents):
            output, self.contents = self.contents, output
            return output
        for _ in range(times):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            output.append(ball)
        return output


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        balls_drawn = Counter(copy.deepcopy(hat).draw(num_balls_drawn))
        for ball, count in expected_balls.items():
            if balls_drawn[ball] < count:
                break
        else:
            successes += 1
    return successes / num_experiments
