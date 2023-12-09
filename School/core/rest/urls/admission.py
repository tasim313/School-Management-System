from django.urls import path
from core.rest.views import admission

urlpatterns = [
    path('',
        admission.SchoolAdmissionView.as_view(),
        name='school-website-information-create'
    ),
]
