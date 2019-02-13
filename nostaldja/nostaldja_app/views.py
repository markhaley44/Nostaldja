from django.shortcuts import render
from django.http import HttpResponse
from .models import Decades, Fads


def helloIndex(request):
    return HttpResponse("ello!")


def decades_list(request):
    context = {'decades': Decades.objects.all()}
    return render(request, 'nostaldja/decades_list.html', context)


def decades_show(request, id):
    context = {'decades': Decades.objects.all(id=id)}
    return render(request, 'nostaldja/decades_show.html', {'decades': decades})
