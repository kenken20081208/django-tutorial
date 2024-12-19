from .models import Event2
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse


def index(request):
    all_event2 = Event2.objects.all()
    context = {"all_event2": all_event2}
    return render(request, "event2/index.html", context)


def pepe(request):
    title = request.POST.get("title")
    new_event2 = Event2()
    new_event2.title = title
    # new_event2.title = "Event2"
    new_event2.save()

    # all_event2 = Event2.objects.all()
    return HttpResponseRedirect(reverse("event2:index"))
