from django.http import HttpResponse


def pepe(request):
    return HttpResponse("Hello, world. You're at the event pepe.")
