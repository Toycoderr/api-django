from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from authentication.models import CustomUser
from django.conf import settings
import jwt, datetime

class Register(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            return Response({'detail': 'User not found!'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'detail': 'Incorrect password!'}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256') 

        response = Response({'email': email, 'message': 'Logged in successfully'})
        response.set_cookie(key='jwt', value=token, httponly=True)  # Set cookie here

        return response
        
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        return Response({"jwt": token})
    
class LogoutView(APIView):

    def post(self, request):
        response = Response()
        # Xóa cookie chứa JWT token
        response.delete_cookie('jwt')
        response.data = {
            'messange': 'success'
        }
        return response