import re

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .usuario_form import PerfilForm


def validou_email(email):
    regex = '^(\w+)@[a-z]+(\.[a-z]+){1,2}$'

    if (re.search(regex, email)):
        return True
    else:
        return False

def criar_conta(request):
    if request.method == 'POST':
        profile = PerfilForm(request.POST)
        if profile.is_valid():

            usr = User.objects.create_user(
                first_name = profile.cleaned_data['first_name'],
                last_name = profile.cleaned_data['last_name'],
                username = profile.cleaned_data['username'],
                email = profile.cleaned_data['email'],
                password = profile.cleaned_data['password'],
            )
            usr.save()
            return redirect('login')

        else:
            return render(request, 'contas/criar_conta.html', {'form':profile})
    else:
        return render(request, 'contas/criar_conta.html', {'form':PerfilForm()})

def htmx_valida_username(request):
    username_digitado = request.POST.get('username')
    if len(username_digitado)<5:
        return HttpResponse("<label style='color:red;'>Tamanho mínimo de 5 caracteres.</label>")
    elif User.objects.filter(username=username_digitado):
        return HttpResponse("<label style='color:red;'>Usuário indisponível.</label>")
    else :
        return HttpResponse("<label style='color:green;'>Usuário disponível.</label>")

def htmx_valida_senha(request):
    passwordd_confirm = request.POST.get('pwd_confirm')
    password = request.POST.get('password')

    if passwordd_confirm != password:
        return HttpResponse("<label style='color:red;'>As senhas não coincidem.</label>")
    else:
        return HttpResponse("")

def htmx_valida_email(request):
    email = request.POST.get('email')

    if not validou_email(email):
        return HttpResponse("<label style='color:red;'>E-mail inválido.</label>")
    if User.objects.filter(email=email):
        return HttpResponse("<label style='color:red;'>E-mail já cadastrado.</label>")
    else:
        return HttpResponse("")

