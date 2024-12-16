from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.index, name="index"),
    path("edit/", views.edit, name="edit"),
]
