from django.shortcuts import render
from website.models import *

def index(request):
    if request.method == 'POST':
        data = Pessoas()
        data.nome = request.POST['nome']
        data.sobrenome = request.POST['sobrenome']
        data.data_de_nascimento = request.POST['data_de_nascimento']
        data.cpf = request.POST['cpf']
        data.cep = request.POST['cep']
        data.item_de_doacao = request.POST['item_de_doacao']
        data.save()

        args = {
            'sucesso': 'Você conseguiu se cadastar com sucesso!'
        }

        return render(request, 'index.html', args)

    return render(request, 'index.html')

def listar_cadastrados(request):
    listar_cadastrados = Pessoas.objects.all()
    args = {
        'listar_cadastrados': listar_cadastrados
    }
    return render(request, 'listar_cadastrados.html', args)
