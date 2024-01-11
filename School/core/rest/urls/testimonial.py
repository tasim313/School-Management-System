from django.urls import path

from core.rest.views.testimonial import (
    TestimonialsAPIView, 
    TestimonialsListView,
    TestimonialsUpdateAPIView,
    TestimonialsDestroy
)

urlpatterns = [

    path(
        "",
        TestimonialsAPIView.as_view(),
        name="school-testimonial-create",
    ),

    path(
        "<uuid:uid>/",
        TestimonialsUpdateAPIView.as_view(),
        name="school-testimonial-update",
    ),

    path(
        "<slug:school_slug>/",
        TestimonialsListView.as_view(),
        name="school-testimonial-list",
    ),
    
    path(
        "<slug:school_slug>/<uuid:uid>/",
        TestimonialsDestroy.as_view(),
        name="school-testimonial-delete",
    ),
]