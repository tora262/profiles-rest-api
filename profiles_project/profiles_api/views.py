from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
    Test Api view
    """

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