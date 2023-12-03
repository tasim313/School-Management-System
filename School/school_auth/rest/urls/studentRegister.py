from django.urls import path
from school_auth.rest.views import studentRegister

urlpatterns = [
    path('', 
         studentRegister.StudentRegisterAPIView.as_view(),
         name='school-student-create'),
]