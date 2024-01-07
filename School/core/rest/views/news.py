from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.models import NewsEvents

from core.rest.serializers.news import NewsEventCreateSerializer, NewsEventUpdateSerializer, NewsEventListSerializer



class NewsEventAPIView(generics.CreateAPIView):
    serializer_class = NewsEventCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            response_data = {
                "message": "News Events Create successful.",
                "data": serializer.data,
            }
            return Response(
                response_data, status=status.HTTP_201_CREATED, headers=headers
            )
        except serializers.ValidationError as e:
            error_data = {
                "message": "News Events Create  failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class NewsEventListView(generics.ListAPIView):
    queryset = NewsEvents.objects.all()
    serializer_class = NewsEventListSerializer

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(school__slug=school_slug)


class NewsEventUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NewsEventUpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"
    allowed_methods = [
        "PUT",
        "PATCH",
    ]

    def get_queryset(self):
        return NewsEvents.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                "message": "News Events update successful.",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            error_data = {
                "message": "News Events update failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save(user_updated=self.request.user)



class NewsEventDestroy(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = NewsEvents.objects.all()
    serializer_class = NewsEventListSerializer
    lookup_field = "uid"
    
    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(school_admission__slug=school_slug)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
