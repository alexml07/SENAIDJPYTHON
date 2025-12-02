from django.shortcuts import render
# from django.http import HttpResponse
var_texto='SENAI'

def home(request):
    return render(request, 'page/home.html', context={
        'nome': var_texto,
    })

def receita(request):
    return render(request, 'page/receita-view.html', context={'nome': var_texto,})

# Create your views here.
