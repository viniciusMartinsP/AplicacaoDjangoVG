from django.contrib.admin.templatetags.admin_list import ResultList
from django.shortcuts import render

from blog.models import Post


# Create your views here.
def my_view(request):
    artigos = Post.objects.all()
    context = {
        'artigos': artigos,
    }
    return render(request, 'testes/primeiro_teste.html', context)

