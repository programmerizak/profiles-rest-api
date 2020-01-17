from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status#To return status code
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View Allow Us To Define Our Application Logic For This Endpoint"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """ get request is used to retrive a list or a particular object"""
        an_apiview = [
        'Uses HTTP methods as function(get,post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLS',

        ]
        """ All HTTP api request(get,post,put,patch,delete) must return a json response object which is a list or a dict"""
        return Response({'message':'Hello !','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello ! {name}'#How u assign variable in strings
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """Handle updating an object completly it do it to particular object,so if you edit first and last name and you
        only input the first name and leave the last name blank, then it will update it in the database and leave it blank"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object, it will only update the field that where provided in the request, so
        if u are updating first and last name and u only provide the first name and leave the last name as it is, then i will
        create a new record of just the first name and leave the initial lastname that were they b4"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
