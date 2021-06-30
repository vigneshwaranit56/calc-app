from calcapp.models import OperationsModel
from calcapp.calclogic.UserDefinedException import *


class CalculationOperation:

    def __init__(self, operationsModel):
        self.operationsModel = operationsModel

    def add(self):
        if int(self.operationsModel.operand2) < 0 and int(self.operationsModel.operand1) < 0:
            raise NonNegativeNUmber
        return int(self.operationsModel.operand1) + int(self.operationsModel.operand2)

    def sub(self):
        if int(self.operationsModel.operand2) < 0 and int(self.operationsModel.operand1) < 0:
            raise NonNegativeNUmber
        return int(self.operationsModel.operand1) - int(self.operationsModel.operand2)

    def mul(self):

        return int(self.operationsModel.operand1) * int(self.operationsModel.operand2)

    def div(self):
        if int(self.operationsModel.operand2) == 0:
            raise NumberNotBeAsZero
        return int(self.operationsModel.operand1) / int(self.operationsModel.operand2)
    def mod(self):
        if int(self.operationsModel.operand2) == 0:
            raise NumberNotBeAsZero
        return int(self.operationsModel.operand1) % int(self.operationModel.operand2)   

    def do_operation(self):
        if self.operationsModel.operation == 'add':
            return self.add()
        elif self.operationsModel.operation == 'sub':
            return self.sub()
        elif self.operationsModel.operation == 'mul':
            return self.mul()
        elif self.operationsModel.operation == 'div':
            return self.div()
        elif self.operationsModel.operation == 'mod':
            return self.mod()
        else:
            raise OperationNotFound
