from django.shortcuts import render
from receitas.fabrica.receitasFake import gen_fake_receita
# from django.http import HttpResponse

# Create your views here.
var_texto='SENAI'

def home(request):
    return render(request, 'page/home.html', context={
        'nome': var_texto,
        'receitas': [gen_fake_receita()
        for _ in range(50)],
    })

def receita(request):
    return render(request, 'page/receita-view.html', context={'nome': var_texto, 'receita': gen_fake_receita()})

# Create your views here.
