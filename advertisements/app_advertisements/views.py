from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisements


def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements' : advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def advertisements_post(request):
    return render(request, 'advertisement-post.html')


def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    return render(request, 'register.html')
