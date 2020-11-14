from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
class inicio(generic.TemplateView):  
    template_name = "inicio.html"
   
