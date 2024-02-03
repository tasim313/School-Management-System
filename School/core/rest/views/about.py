from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from ..serializers.about import (
    WebsiteAboutSerializer,
    WebsiteAboutFileSerializer,
    WebsiteFunFactContentSerializer,
    WebsiteAboutWinningAwardsSerializer,
    AboutListSerializer
)
from ...models import WebsiteAbout, WebsiteAboutFile, WebsiteAboutWinningAwards, WebsiteFunFactContent

from common.choice import Status


class SchoolWebsiteAboutInformationAPIViewListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteAboutSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = WebsiteAbout.objects.filter(
            status=Status.Active,
            website_about_content__slug=school_slug,
        ).select_related(
            "website_about_content"
        )

        return queryset


class SchoolWebsiteAboutInformationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteAboutSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
       
        school_slug = self.kwargs.get("school_slug", None)

        about = WebsiteAbout.objects.filter(
            status=Status.Active,
            website_about_content__slug=school_slug,
        ).select_related(
            "website_about_content"
        )

        return about



class WebsiteAboutFileListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteAboutFileSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = WebsiteAboutFile.objects.filter(
            status=Status.Active,
             about__website_about_content__slug=school_slug,
        ).select_related(
            "about"
        )

        return queryset


class WebsiteAboutFileRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteAboutFileSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
       
        school_slug = self.kwargs.get("school_slug", None)

        about_file = WebsiteAboutFile.objects.filter(
            status=Status.Active,
             about__website_about_content__slug=school_slug,
        ).select_related(
            "about"
        )

        return  about_file



class  WebsiteFunFactContentListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteFunFactContentSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset =  WebsiteFunFactContent.objects.filter(
            status=Status.Active,
            about_info__website_about_content__slug=school_slug,
        ).select_related(
            "about_info"
        )

        return queryset


class  WebsiteFunFactContentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteFunFactContentSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
       
        school_slug = self.kwargs.get("school_slug", None)

        content=  WebsiteFunFactContent.objects.filter(
            status=Status.Active,
            about_info__website_about_content__slug=school_slug,
        ).select_related(
            "about_info"
        )

        return content



class WebsiteAboutWinningAwardsListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteAboutWinningAwardsSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = WebsiteAboutWinningAwards.objects.filter(
            status=Status.Active,
            school_award__website_about_content__slug=school_slug,
        ).select_related(
            "school_award"
        )

        return queryset


class WebsiteAboutWinningAwardsRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteAboutWinningAwardsSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
       
        school_slug = self.kwargs.get("school_slug", None)

        award = WebsiteAboutWinningAwards.objects.filter(
            status=Status.Active,
            school_award__website_about_content__slug=school_slug,
        ).select_related(
            "school_award"
        )

        return award


class AboutListView(generics.ListAPIView):
    serializer_class = AboutListSerializer

    def get_queryset(self):
        website_about_instance = WebsiteAbout.objects.first()
        website_about_file_instances = WebsiteAboutFile.objects.all()
        website_fun_fact_content_instance = WebsiteFunFactContent.objects.first()
        website_about_winning_awards_instance = WebsiteAboutWinningAwards.objects.first()

        # Combine related instances into a single queryset
        queryset = list(website_about_instance) + list(website_about_file_instances) + list(website_fun_fact_content_instance) + list(website_about_winning_awards_instance)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)