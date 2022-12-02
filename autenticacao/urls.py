from django.urls import path

from . import views

urlpatterns = [
    path('', views.processa_login, name="login"),
    path('autenticacao/processa_logout/', views.processa_logout, name="logout"),
    path('autenticacao/processa_redirect_home/', views.processa_redirect_home, name="ir_home"),
]

