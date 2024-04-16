from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'example/index.html', context)