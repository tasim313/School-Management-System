from django.urls import path, include

urlpatterns = [
     path("api/school-admin-app/", include("SchoolAdminApp.rest.urls")),
]