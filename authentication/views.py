from rest_framework import viewsets
from authentication.models import CustomUser
from api_authentication.serializers import CustomUserSerializer
from authentication.permissions import CustomUserPermission

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [CustomUserPermission]