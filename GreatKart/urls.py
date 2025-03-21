from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import Home

urlpatterns = [
    path("jeena/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", Home.as_view(), name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
