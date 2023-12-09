from django.urls import path
from core.rest.views import admission

urlpatterns = [
    path('',
        admission.SchoolAdmissionView.as_view(),
        name='school-admission-list-create'
    ),
    path('<uuid:uid>/',
        admission.SchoolAdmissionDetail.as_view(),
        name='school-admission-detail'
    ),
]
