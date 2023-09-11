import openai
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chat_gpt.serializers import ChatBotSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ChatBotView(APIView):
    authentication_classes = [TokenAuthentication]  # Sử dụng xác thực Token
    permission_classes = [IsAuthenticated]  # Yêu cầu đăng nhập để truy cập

    def post(self, request):
        openai.api_key = settings.OPENAI_API_KEY

        serializer = ChatBotSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            response = self.ask_openai(message)  # Gọi hàm ask_openai

            response_data = {
                'message': message,
                'response': response
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def ask_openai(self, message):
        conversation = [
            {'role': 'system', 'content': 'Translate the following English text to VietNames.'},
            {'role': 'system', 'content': 'You are an helpful assistant.'},
            {'role': 'user', 'content': message},
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        answer = response['choices'][0]['message']['content'].strip()
        return answer