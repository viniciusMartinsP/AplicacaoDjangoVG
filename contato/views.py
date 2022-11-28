from django.shortcuts import render


# Create your views here.
def contato(request):
    return render(request, 'contato/contato.html')

def contact_form(request):
    context = {
        
    }
    return render(request, 'contato/contato.html',context)