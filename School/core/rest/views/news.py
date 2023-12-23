from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.models import NewsEvents

from core.rest.serializers.news import NewsEventListSerializer


class NewsEventList(ListCreateAPIView):
    queryset = NewsEvents.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = NewsEventListSerializer
