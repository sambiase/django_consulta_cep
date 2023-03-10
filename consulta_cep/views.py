from django.shortcuts import render, redirect
import requests


def main_view(request):
    return render(request, 'index.html')


def modal(request):
    return render(request, 'modal.html')


def consulta_cep(request):
    try:

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
    except ValueError:
        return redirect(main_view)
