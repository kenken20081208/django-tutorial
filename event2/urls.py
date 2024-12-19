from django.urls import path

from . import views

app_name = "event2"

urlpatterns = [
    path("pepe/", views.pepe, name="pepe"),
    path("index/", views.index, name="index"),
]
