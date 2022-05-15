
from PyQt5 import QtWidgets, uic
import sys

from validator import Validator
from plotter import Plotter


class MainWindow(QtWidgets.QMainWindow):
    def loadUI(self):
        uic.loadUi('design.ui', self)

    def initButtons(self):
        self.plotBtn.setEnabled(False)
        self.plotBtn.clicked.connect(self.plot)
        self.clrBtn.clicked.connect(self.clearInputs)

    def initTextFields(self):
        self.expression.textChanged.connect(self.validateInput)
        self.min_value.textChanged.connect(self.validateInput)
        self.max_value.textChanged.connect(self.validateInput)

    def initUi(self):
        self.loadUI()
        self.initButtons()
        self.initTextFields()
        self.show()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUi()
        self.plotter = Plotter()
        self.validator = Validator()

    def plot(self):
        self.plotter.plot(self.expression.text(),
                          self.min_value.text(), self.max_value.text())

    def clearInputs(self):
        self.expression.setText("")
        self.min_value.setText("")
        self.max_value.setText("")

    def setWidgetStyle(self, widget, valid):
        if valid:
            widget.setStyleSheet("color : green")
        else:
            widget.setStyleSheet("color : red")

    def validateExpression(self):
        expression = self.expression.text()
        self.validExpression = expression.strip(
        ) != "" and self.validator.validExpression(expression)
        self.setWidgetStyle(self.expression, self.validExpression)

    def validateRange(self):
        min_value, max_value = self.min_value, self.max_value
        self.validRange = self.validator.validRange(
            min_value.text(), max_value.text())
        self.setWidgetStyle(min_value, self.validRange)
        self.setWidgetStyle(max_value, self.validRange)

    def giveUserResponse(self):
        self.validateExpression() 
        self.validateRange()

    def validateInput(self):
        validInput = self.validator.validInput(
            self.expression.text(), self.min_value.text(), self.max_value.text())
        self.giveUserResponse()
        self.plotBtn.setEnabled(validInput)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
