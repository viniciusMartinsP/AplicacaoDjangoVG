from django.db import models

CHOICE_ASSUNTO = [
    ('','SELECIONE UM ASSUNTO'),
    ('descontos','Descontos'),
    ('consultoria','Consultoria'),
    ('freelance','Freelance'),
    ('elogios','Elogios'),
    ('reclamações','Reclamações'),
    ('outros','Outros'),
]

class Contato(models.Model):
    assunto = models.CharField(choices=CHOICE_ASSUNTO, default='',max_length=100)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(max_length=1000)