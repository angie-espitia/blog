from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User


def index(request):
    return render_to_response('../templates/index.html')

def blog(request):
    return render_to_response('../templates/Blog.html')

def problema(request):
    return render_to_response('../templates/problema.html')

def objetivos(request):
    return render_to_response('../templates/objetivos.html')

def justificacion(request):
    return render_to_response('../templates/justificacion.html')

def esquemas(request):
    return render_to_response('../templates/esquemas.html')

def contacto(request):
    return render_to_response('../templates/contact.html')