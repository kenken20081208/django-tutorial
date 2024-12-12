from django.urls import path

from . import views

app_name = "event"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:event_id>/vote/", views.vote, name="vote"),
]
