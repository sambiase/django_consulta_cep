from django.shortcuts import render
import requests


def main_view(request):
    return render(request, 'index.html')


def consulta_cep(request):
    cep = request.POST.get('cep')
    data = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
    res_list = [
        data['logradouro'], data['bairro'],
        data['localidade'], data['uf']
    ]
    context = {
        'res_list': res_list
    }
    return render(request, 'index.html', context)
