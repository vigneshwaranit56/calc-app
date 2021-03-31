from collections import namedtuple

from django.db import models


class OperationsModel(models.Model):
    operand1 = models.FloatField()
    operand2 = models.FloatField()
    operation = models.CharField(max_length=12)
    answer = models.FloatField(default=0)

    def __str__(self):
        return "the operation is {} the first operand  {} and the second operand {} then the result is {}".format(
            self.operation, self.operand1, self.operand2,
            self.answer)

    def dict2obj(self):
        return namedtuple('OperationsModel',self.keys())(*self.values())

    def __setattr__(self, key, value):
        print(f"__setattr__({key}, {value})")
        object.__setattr__(self, key, value)

