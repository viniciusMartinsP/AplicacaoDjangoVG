from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def processa_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            context = {
                'username':username,
                'password':password,
            }
            messages.add_message(request=request, message="Usuário ou senha incorretos", level=messages.ERROR)
            return render(request, 'autenticacao/login.html', context)
    return render(request, 'autenticacao/login.html')

def processa_logout(request):

    # Este trecho de código serve para limpar o storage de messages, código na própria 
    # biblioteca do DJANGO
    storage = messages.get_messages(request)
    
    for messagem in storage:
        pass
    messages.add_message(request=request, message="Logoff realizado", level=messages.ERROR)
    logout(request)
    return redirect("login")

def processa_redirect_home(request):
    return redirect("home")