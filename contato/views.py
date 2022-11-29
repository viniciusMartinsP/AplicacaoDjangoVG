from django.contrib import messages
from django.core.mail import BadHeaderError, EmailMultiAlternatives, send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from contato.contato_form import FormContato
from core import settings


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
            try:
                enviar_email_com_template(contato)
                messages.success(request, "Mensagem encaminhada com sucesso")
                return render(request, 'contato/contato.html', context)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        else:
            context = {
                'form': contato
            }
            return render(request, 'contato/contato.html', context)

    return render(request, 'contato/contato.html', context)

def enviar_email(contato):
    # RECUPER AS INFORMAÇÕES DO FORMULÁRIO
    send_mail(contato.cleaned_data['assunto'],
              contato.cleaned_data['mensagem'],
              settings.EMAIL_HOST_USER,
              [contato.cleaned_data['email']],
              fail_silently=False)

def enviar_email_com_template(contato):
    html_content = render_to_string(
        'email_templates/confirmacao_mensagem.html',
            {'nome':contato.cleaned_data['nome'],
             'assunto':contato.cleaned_data['assunto']})

    # Retira as tags HTML's
    text_content = strip_tags(html_content)
    
    # Responsável por persistir as informações no Banco de Dados
    obj_contato = contato.save()
    obj_contato.save()

    # 
    msg = EmailMultiAlternatives(contato.cleaned_data['assunto'],
                                 text_content,
                                 settings.EMAIL_HOST_USER,
                                 [contato.cleaned_data['email']])

    msg.attach_alternative(html_content, "text/html")
    msg.send()