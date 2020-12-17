from django.shortcuts import render
from carsapp.serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cars
from django.http import Http404


# Create your views here.
class CarDetails(APIView):

    def post(self, request, format=None):

        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        cars = Cars.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class CarList(APIView):

    def get_cars(self, pk):
        try:
            return Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cars = self.get_cars(pk)
        serializer = CarSerializer(cars)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cars = self.get_cars(pk)
        serializer = CarSerializer(cars, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cars = self.get_cars(pk)
        cars.delete()
        return Response('The item has been deleted')