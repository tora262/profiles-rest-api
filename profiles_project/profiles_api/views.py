from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from . import serializers

class HelloApiView(APIView):
    """
    Test Api view
    """
    # hello_serializer = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Return a list of APIView features
        """
        an_apiview = [
            'Use HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Give you the most control over your application logic',
            'Is mapped manually to URL',
        ]

        return Response({'message' : 'Hello', 'an_apiview' : an_apiview})


    def post(self, request):
        """
        Create a hello message with our name
        """
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            print(name)
            message = f'Hello {name}, your email is {email}'

            print(message)
            return Response({"message" : message})
        else:
            print("error")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """
        Handle updating an object
        """
        return Response({"method" : "PUT"})

    def patch(self, request, pk=None):
        """
        Handle a partial update of an object
        """

        return Response({"method" : "PATCH"})


    def delete(self, request, pk=None):
        """
        Handle a delete of update
        """
        return Response({"method":"DELETE"})

