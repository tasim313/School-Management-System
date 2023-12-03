from django.urls import path
from school_auth.rest.views import schoolAdminRegister

urlpatterns = [
    path('', 
         schoolAdminRegister.SchoolAdminRegisterAPIView.as_view(),
         name='school-admin-create'),
]