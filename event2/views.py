from event2 import models  #
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def list(request):
    # ↓Event2の中に入っているデータをすべてall_event2に入れる
    all_event2 = models.Event2.objects.all()
    # ↓all_event2という辞書を作ってその中に内容を入れる
    context = {"all_event2": all_event2}
    # contextにデータが全部入っているので、それをすべてHTMLに送る
    return render(request, "event2/list.html", context)


def pepe(request):
    # ↓HTMLの中のtitleという名前のものを探して、HTMLのtitleの内容をtitleという関数の中に保存する
    title = request.POST.get("title")
    date = request.POST.get("date")
    new_event2 = models.Event2(date=date, title=title)
    # ↓Event2というテーブルのtitleというカラムの中にさっき入ったデータをtitleという関数に入れる
    new_event2.save()

    # ここでindexの関数に飛ぶ
    return HttpResponseRedirect(reverse("event2:list"))


def index(request):
    return render(request, "event2/index.html")


def delete(repuest, event_id):
    event2 = models.Event2.objects.get(id=event_id)
    event2.delete()
    return HttpResponseRedirect(reverse("event2:list"))
