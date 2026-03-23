from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá professor! Sou sua aluna Sarah Beatriz em SO!")
