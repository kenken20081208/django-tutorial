from django.urls import path

from . import views

urlpatterns = [
    path("pepe", views.pepe, name="pepe"),
]
