from rest_framework import response, status
from api_authentication.serializers import CustomUserSerializer
from rest_framework.generics import GenericAPIView

class CustomUserAPIView(GenericAPIView):
    serializer_class = CustomUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)