from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(response):
    person = {'name':'laxmi','age':25}
    return Response(person)