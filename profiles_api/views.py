from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View Allow Us To Define Our Application Logic For This Endpoint"""

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
