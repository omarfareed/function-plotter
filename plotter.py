from validator import Validator
from matplotlib.pyplot import plt
import numpy as np


class Plotter():
    def __init__(self):
        self.validator = Validator()

    def _evaluate(self, expression, x):
        expression = expression.replace('x', str(x)).replace('^', '**')
        return eval(expression)

    def _getGraphSets(self, expression, x_min, x_max):
        step = (x_max - x_min) / 10000
        x = [round(i, 6) for i in np.arange(x_min, x_max, step)]
        y = [self._evaluate(expression, i) for i in x]
        return x, y

    def _plot(self, expression, x_min, x_max):
        x, y = self._getGraphSets(expression, x_min, x_max)
        plt.plot(x, y)
        plt.show()

    def plot(self, expression, min, max):
        if not self.validator.valid(expression):
            raise ValueError('Invalid expression')
        self._plot(expression, min, max)
