from django.http import HttpResponse
from django.shortcuts import render

from todo import models


def index(request):
    all_todo = models.Todo.objects.all()
    context = {"aho": "baka", "all_todo": all_todo}
    return render(request, "todo/index.html", context)


def edit(request):
    return HttpResponse("Hello, world. You're at the todo2 edit.")


def baka(request):
    new_todo = models.Todo()
    new_todo.title = "いけけけ"
    new_todo.save()

    all_todo = models.Todo.objects.all()
    return HttpResponse(all_todo)
