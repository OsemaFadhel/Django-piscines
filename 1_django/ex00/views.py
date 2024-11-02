from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def markdown_cheatsheet(request):
    return render(request, 'ex00/markdown.html')
