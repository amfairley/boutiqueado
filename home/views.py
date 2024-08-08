from django.shortcuts import render


def index(request):
    '''Docstring'''
    return render(request, 'home/index.html')
