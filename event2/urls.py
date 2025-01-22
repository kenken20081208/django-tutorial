from django.urls import path

from . import views

app_name = "event2"

urlpatterns = [
    path("pepe/", views.pepe, name="pepe"),
    path("index/", views.index, name="index"),
    path("list/", views.list, name="list"),
    path("delete/<int:event_id>", views.delete, name="delete"),
]
