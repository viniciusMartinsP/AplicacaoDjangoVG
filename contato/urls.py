from django.urls import path

from . import views

urlpatterns = [
    path('',views.contato, name='contato'),
    path('mensagem',views.contact_form, name='mensagem'),
]
