from django.urls import include, path


urlpatterns = [ 
    path("school/student/registration", include("school_auth.rest.urls.studentRegister")),
    path("login/", include("school_auth.rest.urls.Login")),
    path("school/admin/registration", include("school_auth.rest.urls.SchoolAdminRegister")),
    path("school/teacher/registration", include("school_auth.rest.urls.TeacherRegister")),
]