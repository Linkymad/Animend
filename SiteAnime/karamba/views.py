from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

class HomePage(View):
    def get(self, request):
        anime_list = Anime.objects.order_by('-id').filter(check_True=2)[:5]
        return render(request, 'karamba/home.html', {'anime_list': anime_list})



class PageAnimend(View):
    def get(self, request):
        anime = Anime.objects.filter(check_True=2)
        return render(request, 'karamba/animend.html', {'anime': anime})


class PageAniwill(View):
    def get(self, request):
        anime = Anime.objects.filter(check_True=1)
        return render(request, 'karamba/aniwill.html', {'anime': anime})


class AnimeDetailPage(View):

    def get(self, request, slug):
        anime = Anime.objects.get(url=slug)
        return render(request, "karamba/AnimeDetailPage.html", {'anime': anime})

