from django.contrib import admin
from django.urls import include, path
from inicio.views import inicio
urlpatterns = [
    path('', inicio.as_view(), name='inicio')
]
