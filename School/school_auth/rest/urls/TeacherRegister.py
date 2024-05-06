from django.urls import path
from school_auth.rest.views import teacherRegister

urlpatterns = [
    path('', 
         teacherRegister.TeacherRegisterAPIView.as_view(),
         name='school-teacher-create'),
]