from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    var_texto='SENAI'

    return render(request, 'home.html', context={
        'nome': var_texto,
    })


# Create your views here.
