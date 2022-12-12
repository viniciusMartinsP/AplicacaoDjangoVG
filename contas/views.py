import re

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

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
    context = {'error_username':'Username indisponível', 'st_submit':'disabled', 'cor':'red'}
    username_digitado = request.POST.get('username')
    
    if not User.objects.filter(username=username_digitado):
        context['error_username'] = 'Username disponível'
        context['cor']='green'
    
    if PerfilForm(request.POST).is_valid():
        context['st_submit']=''

    str_template = render_to_string('contas/feedback_form_validation.html', context)
    return HttpResponse(str_template)

def htmx_valida_senha(request):
    context = {'error_pwd':'As senhas não coincidem', 'st_submit':'disabled', 'cor':'red'}
    password_confirm = request.POST.get('pwd_confirm')
    password = request.POST.get('password')

    if password_confirm == password and PerfilForm(request.POST).is_valid():
        context['error_pwd']=''
        context['st_submit']=''
        
    str_template = render_to_string('contas/feedback_form_validation.html', context)
    return HttpResponse(str_template)
    

def htmx_valida_email(request):
    context = {'usr_email':'E-mail inválido ou já cadastrado','st_submit':'disabled'}
    email = request.POST.get('email')

    if not validou_email(email):
        return HttpResponse("<label style='color:red;'>E-mail inválido.</label>")
    
    if User.objects.filter(email=email):
        return HttpResponse("<label style='color:red;'>E-mail já cadastrado.</label>")
    else:
        context['usr_email']="E-mail disponível"
        context['st_submit']=''
        str_template = render_to_string('contas/feedback_form_validation.html', context)
        return HttpResponse(str_template)

