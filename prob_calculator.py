import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        for i, j in kwargs.items():
            for k in range(0, j):
                self.contents.append(i)

    def draw(self, n):
        if n >= len(self.contents):
            drawn = self.contents
            self.contents = list()
            return drawn
        else:
            drawn = random.sample(self.contents, n)
            for i in drawn:
                self.contents.remove(i)
            return drawn
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    success = 0
    expected = list()
    for i in list(expected_balls):
        j = expected_balls[i]
        for k in range(0, j):
            expected.append(i)

    for i in range(0, num_experiments):
        testin = expected
        testhat = copy.deepcopy(hat)
        testout = testhat.draw(num_balls_drawn)
        fail = 0
        for j in testin:
            if j in testout:
                testout.remove(j)
            else:
                fail = 1

        success += (1 - fail)


    return (success/num_experiments)
