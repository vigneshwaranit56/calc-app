from rest_framework import serializers
from calcapp.models import OperationsModel


class OperationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationsModel
        fields = ('id','operand1', 'operand2','operation','answer')
