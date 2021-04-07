from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from calcapp.models import OperationsModel
from calcapp.serializers import OperationModelSerializer
from rest_framework.decorators import api_view
from calcapp.calclogic.CalculationAppLogic import CalculationOperation


@api_view(['GET', 'POST', 'DELETE'])
def operations_list(request):
    if request.method == 'GET':  # list of operation performed
        operation_dict = OperationsModel.objects.all()
        operation_model_serializer = OperationModelSerializer(operation_dict, many=True)
        return JsonResponse(operation_model_serializer.data, safe=False)
    elif request.method == 'POST':  # operation
        operation_dict = JSONParser().parse(request)
        operation_model = OperationsModel.dict2obj(operation_dict)
        calc_app = CalculationOperation(operation_model)
        operation_dict['answer'] = calc_app.do_operation()
        print(operation_dict)
        operation_model_serializer = OperationModelSerializer(data=operation_dict)
        if operation_model_serializer.is_valid():
            operation_model_serializer.save()
            return JsonResponse(operation_model_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(operation_model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':  # Delete list of all the operation
        count = OperationsModel.objects.all().delete()
        return JsonResponse({'message': '{} Calculation were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def operation_detail(request, pk):
    try:
        operation_model = OperationsModel.objects.get(pk=pk)
    except OperationsModel.DoesNotExist:
        return JsonResponse({'message': 'The calculation entry does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # particular operation get
        operation_model_serializer = OperationModelSerializer(operation_model)
        return JsonResponse(operation_model_serializer.data)
    elif request.method == 'DELETE':  # particular operation delete
        operation_model.delete()
        return JsonResponse({'message': 'calculation entry was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
