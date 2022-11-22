from django.shortcuts import render


def get_boostrap(request):
    return render(request, 'exemplos/03_grids.html')

def collapse(request):
    return render(request, 'exemplos/collapse.html')

def flexbox(request):
    return render(request, 'exemplos/flexbox.html')
