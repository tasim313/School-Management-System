from django.urls import path
from core.rest.views.blog import (
    BlogListCreateAPIView,
    BlogRetrieveUpdateDestroyAPIView,
    BlogTagListCreateView,
    BlogTagRetrieveUpdateView,
    BlogCategoryListCreateView,
    BlogCategoryRetrieveUpdateView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        BlogListCreateAPIView.as_view(),
        name="school-blog-list",
    ),
    path(
        "<uuid:uid>/",
        BlogRetrieveUpdateDestroyAPIView.as_view(),
        name="school-blog-detail",
    ),
    path(
        "tag/",
        BlogTagListCreateView.as_view(),
        name="school-blog-tag-list",
    ),
    path(
        "tag/<uuid:uid>/",
        BlogTagRetrieveUpdateView.as_view(),
        name="school-blog-tag-detail",
    ),
    path(
        "category/",
        BlogCategoryListCreateView.as_view(),
        name="school-blog-category-list",
    ),
    path(
        "category/<uuid:uid>/",
        BlogCategoryRetrieveUpdateView.as_view(),
        name="school-blog-category-detail",
    ),
]
