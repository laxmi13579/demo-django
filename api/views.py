from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import PersonSerializer
from base.models import Person

@api_view(['GET'])
def getPerson(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)