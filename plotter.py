from cmath import exp
from tkinter.tix import MAX
from wsgiref.validate import validator
import matplotlib
from validator import Validator
import matplotlib.pyplot as plt
import numpy as np


class Plotter():
    def __init__(self):
        # init validator object
        self.validator = Validator()

    def evaluate(self, expression, x):
        try:
            expression = expression.replace('x', f'({x})').replace('^', '**')
            val = eval(expression)
            return val
        except:
            # if value is so large or invalid like 0 ^ 0
            return None

    def getGraphPoints(self, expression, x_min, x_max):
        # create x axes points
        x = np.linspace(x_min, x_max, 100000)
        # y axes points using evaluate function
        y = [self.evaluate(expression, i) for i in x]
        return x, y

    def initLabels(self, expression):
        plt.figure(num="2d plotter")
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.title(f'F(X) = {expression.replace(" " , "")}')

    def _plot(self, expression, x_min, x_max):
        x, y = self.getGraphPoints(expression, x_min, x_max)
        self.initLabels(expression)
        plt.plot(x, y)
        plt.show()

    def plot(self, expression, x_min, x_max):
        if not self.validator.validInput(expression, x_min, x_max):
            raise ValueError('Invalid expression')
        self._plot(expression, float(x_min), float(x_max))
