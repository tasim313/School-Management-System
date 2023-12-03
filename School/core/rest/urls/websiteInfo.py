from django.urls import path
from core.rest.views import websiteInfo

urlpatterns = [
    path('', 
         websiteInfo.SchoolWebsiteAPIView.as_view(),
         name='school-website-information-create'),
]