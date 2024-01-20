from rest_framework import permissions
from datetime import timedelta
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from ...models import User

from ..serializers import(
    Login,
    UserSerializer
)




class LoginView(generics.ListCreateAPIView):

    """User can Login system by username and password"""

    permission_classes = (permissions.AllowAny,)
    serializer_class = Login.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        user_serializer = UserSerializer.UserSerializer(user)
        serialized_user = user_serializer.data

        response_data = {
            'message': 'Login successful!',
            'data': {
                'user': serialized_user,
                'access': {
                    'auth_type': 'Bearer',
                    'Bearer': access_token,
                }
            }
        }
        return Response(response_data)