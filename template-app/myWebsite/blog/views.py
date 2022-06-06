from django.shortcuts import render

# Create your views here.
def index(responses):
    return render(responses, 'index.html')