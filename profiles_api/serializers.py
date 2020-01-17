from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializer a name field for testing our api view, they work like django forms"""
    name = serializers.CharField(max_length=10)
