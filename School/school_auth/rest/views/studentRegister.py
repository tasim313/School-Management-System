from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..serializers import Register


class StudentRegisterAPIView(generics.CreateAPIView):
    serializer_class = Register.StudentRegisterSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            response_data = {
                'message': 'Student registration successful.',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        except serializers.ValidationError as e:
            error_data = {
                'message': 'Student registration failed.',
                'errors': e.detail
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
