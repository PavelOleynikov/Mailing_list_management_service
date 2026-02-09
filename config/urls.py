from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("mailing/", include("mailing.urls")),
    path("message/", include("message.urls")),
    path("recipients/", include("recipients.urls")),
    path("", include("main.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
