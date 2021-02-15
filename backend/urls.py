from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from chat.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("api-auth/", include("rest_framework.urls")),
    path("chat/", include("chat.urls")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
