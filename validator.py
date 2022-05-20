import re
# get all special function from math
from math import *
import math
specialFunctions = [function for function in math.__dir__()
                    if not function.startswith('__')]
specialFunctionsRegex = r'|'.join(
    [f'[\s\(]*{function}\s*\(' for function in specialFunctions])


class Validator():
    def __init__(self):
        self.numRegex = r'\-?[0-9]*\.?[0-9]+'
        termRegex = rf'[\s\(]*(({self.numRegex})|[Xx])[\s\)]*'
        print(termRegex)
        self.expressionRegex = re.compile(
            rf'^({termRegex}[\+\-\*\/\^]|{specialFunctionsRegex})*{termRegex}$')

    def numericValue(self, value):
        return re.match(rf'^{self.numRegex}$', f'{value}') is not None

    def validRange(self, x_min, x_max):
        return self.numericValue(x_min) and self.numericValue(x_max) and float(x_min) < float(x_max)

    def validBrackets(self, expression):
        brackets = []
        for i in expression:
            if i == '(':
                brackets.append(i)
            elif i == ')':
                if len(brackets) == 0:
                    return False
                brackets.pop()
        return len(brackets) == 0

    def validExpression(self, expression):
        return re.match(self.expressionRegex, expression) is not None and self.validBrackets(expression)

    def validInput(self, expression, x_min, x_max):
        return self.validExpression(expression) and self.validRange(x_min, x_max)
