from rest_framework import permissions
from datetime import timedelta
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from ...models import User

from ..serializers import(
    Login,
    UserSerializer
)


class LoginView(generics.ListCreateAPIView):

    """User can Login system by username and password"""
    
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = Login.LoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer.UserSerializer(user)
            serialized_user = user_serializer.data

            response_data = {
                'message': 'Login successful!',
                'data': {
                    'user': serialized_user,
                    'access': {
                        'auth_type': 'Bearer',
                        'token': token.key,
                    }
                }
            }
            return Response(response_data)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)