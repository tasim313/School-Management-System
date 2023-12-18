from django.urls import path
from core.rest.views.news import NewsEventList

urlpatterns = [
    path(
        "",
        NewsEventList.as_view(),
        name="school-news-event",
    ),
    # path(
    #     "<uuid:uid>",
    #     NewsEventList.as_view(),
    #     name="school-news-event",
    # ),
]
