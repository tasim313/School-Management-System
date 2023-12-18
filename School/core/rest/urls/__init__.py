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
        "school/gallery/",
        include("core.rest.urls.gallery"),
    ),
]
