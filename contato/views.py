from django.contrib import messages
from django.shortcuts import render

from contato.contato_form import FormContato


# Create your views here.
def contato(request):
    context = {
        'form': FormContato()
    }
    return render(request, 'contato/contato.html', context)


def contact_form(request):
    if request.method == 'POST':
        contato = FormContato(request.POST)
        context = {
            'form': FormContato()
        }
        if contato.is_valid():
            assunto = contato.cleaned_data['assunto']
            mensagem = request.POST.get('mensagem')
            messages.success(request, "Mensagem encaminhada com sucesso")
            return render(request, 'contato/contato.html', context)
        else:
            context = {
                'form': contato
            }
            return render(request, 'contato/contato.html', context)

    return render(request, 'contato/contato.html', context)
