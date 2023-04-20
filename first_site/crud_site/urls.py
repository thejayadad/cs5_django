
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("dunbar/", views.dunbar, name="dunbar"),
    path("<str:name>", views.greet, name="greet")
]
