from django.http import HttpResponse
from django.template import loader

from .models import Event


def vote(request, event_id):
    return HttpResponse("You're voting on event %s." % event_id)


def index(request):
    latest_event_list = Event.objects.order_by("-pub_date")[:5]
    template = loader.get_template("event/index.html")
    context = {
        "latest_event_list": latest_event_list,
    }
    return HttpResponse(template.render(context, request))
