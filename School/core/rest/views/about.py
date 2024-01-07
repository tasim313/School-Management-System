from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status, serializers 

from ..serializers import about
from ...models import WebsiteAbout, WebsiteAboutFile


class SchoolWebsiteAboutInformationAPIView(generics.CreateAPIView):
    serializer_class = about.SchoolAboutInformationCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            response_data = {
                "message": "School Website About Information Create successful.",
                "data": serializer.data,
            }
            return Response(
                response_data, status=status.HTTP_201_CREATED, headers=headers
            )
        except serializers.ValidationError as e:
            error_data = {
                "message": "School Website About Information failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
        

class SchoolWebsiteAboutInformationListView(generics.ListAPIView):
    queryset = WebsiteAbout.objects.all()
    serializer_class = about.SchoolAboutInformationList

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(website_about_content__slug=school_slug)
    


class SchoolWebsiteAboutFileAPIView(generics.ListCreateAPIView):
    serializer_class = about.SchoolAboutFileCreate
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            response_data = {
                "message": "School Website About Image Create successful.",
                "data": serializer.data,
            }
            return Response(
                response_data, status=status.HTTP_201_CREATED, headers=headers
            )
        except serializers.ValidationError as e:
            error_data = {
                "message": "School Website About Image failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
        


class SchoolWebsiteAboutImageListView(generics.ListAPIView):
    queryset = WebsiteAboutFile.objects.all()
    serializer_class = about.SchoolAboutFileList

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(about__website_about_content__slug=school_slug)