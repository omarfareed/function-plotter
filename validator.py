import re


class Validator():
    def __init__(self):
        numRegex = r'\-?[0-9]*\.?[0-9]+'
        termRegex = rf'\(*\s*(({numRegex})|x)\s*\)*'
        self.expressionRegex = re.compile(
            rf'^({termRegex}[\+\-\*\/\^])*{termRegex}$')

    def _validBrackets(self, expression):
        brackets = []
        for i in expression:
            if i == '(':
                brackets.append(i)
            elif i == ')':
                if len(brackets) == 0:
                    return False
                brackets.pop()
        return len(brackets) == 0

    def validate(self, expression):
        return re.match(self.expressionRegex, expression) is not None and self._validBrackets(expression)
