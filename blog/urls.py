from django.conf.urls import url
from django.contrib import admin

from project.views import *

urlpatterns = [
    url(r'^$', index, name='index'),  # /
    url(r'^blog$', blog, name='blog'),  # /blog
    url(r'^problema$', problema, name='problema'),  # /problema
    url(r'^justificacion$', justificacion, name='justificacion'),  # /justificacion
    url(r'^objetivos$', objetivos, name='objetivos'),  # /objetivos
    url(r'^esquemas$', esquemas, name='esquemas'),  # /esquemas
    url(r'^contacto$', contacto, name='contacto'),  # /contacto
]
