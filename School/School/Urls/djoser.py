from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('school/auth/', include('djoser.urls.authtoken')),
    path('jwt/', include('djoser.urls.jwt')),
]