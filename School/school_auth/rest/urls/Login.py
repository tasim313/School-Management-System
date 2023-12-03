from django.urls import path

from ..views import Login


urlpatterns = [
    path('',
         Login.LoginView.as_view(),
         name="auth-login"),
]