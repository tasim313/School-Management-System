from django.urls import path
from core.rest.views.websiteInfo import (
    SchoolWebsiteAPIView,
    WebsiteInformationListView,
    SchoolWebsiteUpdateAPIView
)

urlpatterns = [
    path('', 
         SchoolWebsiteAPIView.as_view(),
         name='school-website-information-create'),
    path("<slug:school_slug>/", WebsiteInformationListView.as_view(), name="school_website_information"),
    path("update/<uuid:uid>/", SchoolWebsiteUpdateAPIView.as_view(), name="school-website-update"),
]