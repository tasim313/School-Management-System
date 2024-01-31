from django.urls import path

from core.rest.views.team import (
   WebsiteTeacherInformationListCreateView,
    WebsiteTeacherInformationRetrieveUpdateDeleteView,
    WebsiteManagingCommitteeMemberInformationListCreateView,
    WebsiteManagingCommitteeMemberInformationRetrieveUpdateDeleteView,
    WebsiteStaffInformationListCreateView,
    WebsiteStaffInformationRetrieveUpdateDeleteView,
    WebSiteFacultyInformationListCreateView,
    WebSiteFacultyInformationRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/teacher/",
       WebsiteTeacherInformationListCreateView.as_view(),
        name="team_teacher_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/teacher/",
        WebsiteTeacherInformationRetrieveUpdateDeleteView.as_view(),
        name="team_teacher_delete",
    ),
    path(
        "<slug:school_slug>/member/",
        WebsiteManagingCommitteeMemberInformationListCreateView.as_view(),
        name="team_member_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/member/",
        WebsiteManagingCommitteeMemberInformationRetrieveUpdateDeleteView.as_view(),
        name="team_member_delete",
    ),
    path(
        "<slug:school_slug>/staff/",
        WebsiteStaffInformationListCreateView.as_view(),
        name="team_staff_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/staff/",
        WebsiteStaffInformationRetrieveUpdateDeleteView.as_view(),
        name="team_staff_delete",
    ),
    path(
        "<slug:school_slug>/faculty/",
        WebSiteFacultyInformationListCreateView.as_view(),
        name="team_faculty_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/faculty/",
        WebSiteFacultyInformationRetrieveUpdateDeleteView.as_view(),
        name="team_faculty_delete",
    ),
]