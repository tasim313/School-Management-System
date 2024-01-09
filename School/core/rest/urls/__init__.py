from django.urls import include, path


urlpatterns = [
    path(
        "school/information/",
        include("core.rest.urls.websiteInfo"),
    ),
    path(
        "school/admission/",
        include("core.rest.urls.admission"),
    ),
    path(
        "school/academic-information/",
        include("core.rest.urls.academic"),
    ),
    path(
        "slider/content/",
        include("core.rest.urls.sliderContent"),
    ),
    path(
        "school/news/",
        include("core.rest.urls.news"),
    ),
    path(
        "school/about/",
        include("core.rest.urls.about"),
    ),
    path(
        "school/blog/",
        include("core.rest.urls.blog"),
    ),
    path(
        "school/social/media/",
        include("core.rest.urls.socialmedia"),
    ),
]
