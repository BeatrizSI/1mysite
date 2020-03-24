from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello Word!")


def contatos(request):
    return HttpResponse("Contatos")


def sobre(request):
    return HttpResponse("Sobre")
