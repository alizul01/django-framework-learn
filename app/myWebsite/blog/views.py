from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return render(request, 'blog.html')

def recent(response):
    return HttpResponse('Halo ini responses dari Recent!')
