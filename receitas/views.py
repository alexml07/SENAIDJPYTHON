from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    var_texto='Receitas Django'
    return render(request, 'home.html', context={
        'nome': var_texto,
    })

def sobre(request):
    return HttpResponse("Sobre nós!")

def receita(request):
    return HttpResponse("As receitas")

# Create your views here.
