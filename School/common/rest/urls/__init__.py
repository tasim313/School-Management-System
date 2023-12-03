from django.urls import include, path


urlpatterns = [ 
    path("school/onboard/", include("common.rest.urls.schoolInformation")),
]