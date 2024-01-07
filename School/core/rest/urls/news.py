from django.urls import path
from core.rest.views.news import NewsEventAPIView,  NewsEventListView, NewsEventUpdateAPIView, NewsEventDestroy

urlpatterns = [
    path(
        "",
        NewsEventAPIView.as_view(),
        name="school-news-events-create",
    ),
    path(
        "<uuid:uid>/",
        NewsEventUpdateAPIView.as_view(),
        name="school-news-events-update",
    ),
    path(
        "<slug:school_slug>/",
        NewsEventListView.as_view(),
        name="school-news-events-list",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        NewsEventDestroy.as_view(),
        name="school-news-events-delete",
    ),
]
