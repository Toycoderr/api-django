from rest_framework import serializers
from django.conf import settings

class ChatBotSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)  # Đảm bảo max_length phù hợp với yêu cầu của bạn

class ChatBotResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    response = serializers.CharField()