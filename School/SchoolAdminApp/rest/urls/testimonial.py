"""URLs for Testimonial API"""

from django.urls import path

from SchoolAdminApp.rest.views.testimonial import (
    TestimonialListCreateView,
    TestimonialRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        TestimonialListCreateView.as_view(),
        name="testimonial-list-create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        TestimonialRetrieveUpdateDeleteView.as_view(),
        name="testimonial-retrieve-update-delete",
    ),
]
