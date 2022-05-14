import matplotlib
from validator import Validator
import matplotlib.pyplot as plt
import numpy as np


class Plotter():
    def __init__(self):
        self.validator = Validator()

    def evaluate(self, expression, x):
        expression = expression.replace('x', f'({x})').replace('^', '**')
        return eval(expression)

    def getGraphPoints(self, expression, x_min, x_max):
        step = (x_max - x_min) / 10000
        x = [round(i, 6) for i in np.arange(x_min, x_max, step)]
        y = [self.evaluate(expression, i) for i in x]
        return x, y

    def _plot(self, expression, x_min, x_max):
        x, y = self.getGraphPoints(expression, x_min, x_max)
        plt.plot(x, y)
        plt.show()

    def validate(self, expression, x_min, x_max):
        return self.validator.validate(expression) and x_min < x_max

    def plot(self, expression, x_min, x_max):
        if not self.validate(expression, x_min, x_max):
            raise ValueError('Invalid expression')
        self._plot(expression, x_min, x_max)
