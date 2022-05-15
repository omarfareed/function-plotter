from tkinter.tix import MAX
from wsgiref.validate import validator
import matplotlib
from validator import Validator
import matplotlib.pyplot as plt
import numpy as np


class Plotter():
    def __init__(self):
        self.validator = Validator()

    def evaluate(self, expression, x):
        expression = expression.replace('x', f'({x})').replace('^', '**')
        val = eval(expression)
        return val

    def getGraphPoints(self, expression, x_min, x_max):
        step = (x_max - x_min) / 10000
        x = [round(i, 6) for i in np.arange(x_min, x_max, step)]
        y = [self.evaluate(expression, i) for i in x]
        return x, y

    def _plot(self, expression, x_min, x_max):
        x, y = self.getGraphPoints(expression, x_min, x_max)
        plt.plot(x, y)
        plt.show()

    def plot(self, expression, x_min, x_max):
        if not self.validator.validInput(expression, x_min, x_max):
            raise ValueError('Invalid expression')
        self._plot(expression, float(x_min), float(x_max))
