from django.urls import path
from common.rest.views import schoolInformation

urlpatterns = [
    path('', 
         schoolInformation.SchoolInformationOnBoardingCreateAPIView.as_view(),
         name='school-information-create'),
    path("list/", schoolInformation.SchoolInformationOnBoardingList.as_view(), name="school-onboard-list"),
    path("<uuid:uid>/", schoolInformation.SchoolInformationOnBoardingRetrieveUpdate.as_view(), name="school-onboard-update"),
]