from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Registration
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework import filters
 
# Create your views here.
class RegistrationList(APIView):
    
    def get(self, request):
        reg = Registration.objects.all()
        serializer = RegistrationSerializer(reg, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RegisterDetails(APIView):
    def get_object(self, pk):
        try:
            return Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk):
        reg = self.get_object(pk)
        serializer = RegistrationSerializer(reg)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        reg = self.get_object(pk)
        serializer = RegistrationSerializer(reg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        reg = self.get_object(pk)
        reg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
 
class SearchListView(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'id', 'first_name']