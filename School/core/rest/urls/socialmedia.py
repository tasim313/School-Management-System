from django.urls import path
from core.rest.views.socialmedia import SocialMediaAPIView,  SocialMediaListView, SocialMediaUpdateAPIView, SocialMediaDestroy

urlpatterns = [
    path(
        "",
        SocialMediaAPIView.as_view(),
        name="school-social-media-create",
    ),
    path(
        "<uuid:uid>/",
        SocialMediaUpdateAPIView.as_view(),
        name="school-social-media-update",
    ),
    path(
        "<slug:school_slug>/",
        SocialMediaListView.as_view(),
        name="school-social-media-list",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        SocialMediaDestroy.as_view(),
        name="school-social-media-delete",
    ),
]