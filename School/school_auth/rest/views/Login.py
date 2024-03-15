from django.utils import timezone

from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from SubscriptionApp.models import Subscription

from school_auth.rest.serializers import (
    Login,
    UserSerializer
)


class LoginView(generics.ListCreateAPIView):
    """User can Log in system by username and password"""

    permission_classes = (permissions.AllowAny,)
    serializer_class = Login.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')

        dev_school_id = True if user.school_id == 1 else False

        if not user.is_superuser or not dev_school_id:
            if not Subscription.objects.filter(
                    school_subscription_id=user.school_id,
                    is_paid=True,
                    end_date__gte=timezone.now().date()
            ).exists():
                return Response(
                    {"error": "You are not subscribed to any plan. Please contact your school admin."},
                    status=status.HTTP_400_BAD_REQUEST
                )

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
