from django.urls import path

from main.apps import MainConfig
from main.views import main_page

app_name = MainConfig.name

urlpatterns = [
    path("", main_page, name="base"),
]
