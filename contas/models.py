from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Perfil (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True, max_length=255)
    foto = models.ImageField(blank=True, null=True, default='', upload_to='static/contas')


# created from 'post_save'
# https://docs.djangoproject.com/en/4.1/ref/signals/
@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    

    