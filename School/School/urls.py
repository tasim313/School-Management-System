from django.conf.urls.static import static
from django.conf import settings

from School.Urls.admin import urlpatterns as admin
from School.Urls.djoser import urlpatterns as djoser
from School.Urls.debug_toolbar import urlpatterns as toolbar
from School.Urls.swagger import urlpatterns as swagger


from School.Urls.common import urlpatterns as common

from School.Urls.school_auth import urlpatterns as authentication
from School.Urls.core import urlpatterns as website
from School.Urls.student import urlpatterns as student


urlpatterns = []

urlpatterns.extend(admin)
urlpatterns.extend(djoser)
urlpatterns.extend(toolbar)
urlpatterns.extend(swagger)

urlpatterns.extend(common)
urlpatterns.extend(authentication)
urlpatterns.extend(website)
urlpatterns.extend(student)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(
        settings.MEDIA_URL_2,
        document_root=settings.MEDIA_ROOT)



