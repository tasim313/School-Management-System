from django.urls import include, path


urlpatterns = [ 
    path("school/information/", include("core.rest.urls.websiteInfo")),
    path('slider/content/', include("core.rest.urls.sliderContent")),
    
]