from django.urls import path
from StudentApp.rest.views.student import (
    StudentInformationListView,
)


urlpatterns = [
    path('<slug:school_slug>/', 
         StudentInformationListView.as_view(),
         name='student-information-list'),
]