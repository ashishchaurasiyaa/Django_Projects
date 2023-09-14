from rest_framework import serializers

class HelloSerilizer(serializers.Serializer):
    """Serilizers a name field for testing our APIView"""
    name = serializers.CharField(max_length=40)
