from django.urls import path
from .views import user


app_name = "chat"

urlpatterns = [path("user/", user, name="create-user")]
