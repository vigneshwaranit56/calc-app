from calcapp.models import OperationsModel
from calcapp.calclogic.UserDefinedException import *


class CalculationOperation:

    def __init__(self, operationsModel):
        self.operationsModel = operationsModel

    def add(self):
        if self.operationsModel.operand2 < 0 and self.operationsModel.operand1 < 0:
            raise NonNegativeNUmber
        return self.operationsModel.operand1 + self.operationsModel.operand2

    def sub(self):
        if self.operationsModel.operand2 < 0 and self.operationsModel.operand1 < 0:
            raise NonNegativeNUmber
        return self.operationsModel.operand1 - self.operationsModel.operand2

    def mul(self):
        if self.operationsModel.operand2 < 0 and self.operationsModel.operand1 < 0:
            raise NonNegativeNUmber
        return self.operationsModel.operand1 * self.operationsModel.operand2

    def div(self):
        if self.operationsModel.operand2 == 0:
            raise NumberNotBeAsZero
        return self.operationsModel.operand1 / self.operationsModel.operand2

    def do_operation(self):
        if self.operationsModel.operation == 'add':
            return self.add()
        elif self.operationsModel.operation == 'sub':
            return self.sub()
        elif self.operationsModel.operation == 'mul':
            return self.mul()
        elif self.operationsModel.operation == 'div':
            return self.div()
        else:
            raise OperationNotFound
