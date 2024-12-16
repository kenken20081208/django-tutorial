from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the todo3 index.")


def edit(request):
    return HttpResponse("Hello, world. You're at the todo3 edit.")
