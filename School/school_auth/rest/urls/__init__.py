from django.urls import include, path


urlpatterns = [ 
    path("school/student/", include("school_auth.rest.urls.studentRegister")),
    path("login/", include("school_auth.rest.urls.Login")),
    path("school/admin/", include("school_auth.rest.urls.SchoolAdminRegister")),
]