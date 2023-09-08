from rest_framework import serializers
from authentication.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=100,min_length=6,write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        
    def create(seft, validate_data):
        return CustomUser.objects.create_user(**validate_data)