from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Code
from rest_framework import viewsets
# Create your views here.

@api_view(['GET'])
def new_session(request):
    """
    Создает новую сессию и выдаетс ссылки писателю и читателю
    """

    code = Code.objects.create()
    return Response(code.pk, status=status.HTTP_200_OK)

@api_view(['POST'])
def edit_code(request, code_id):
    """
    сохраняет код в базу данных
    code_id - id сессии
    """

    code = Code.objects.get(id=code_id)
    code.code = request.data['code']
    code.save()
    return Response(code.code, status=status.HTTP_200_OK)

@api_view(['GET'])
def read_code(request, code_id):
    """
    демонстрирует текущий код
    code_id - id сессии
    """
    code = Code.objects.get(id=code_id)
    return Response(code.code, status=status.HTTP_200_OK)
