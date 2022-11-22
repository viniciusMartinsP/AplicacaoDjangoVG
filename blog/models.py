from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone


# Create your models here.python.
class Post(models.Model):
    autor = models.CharField(max_length = 255)
    titulo = models.CharField(max_length = 255)
    subtitulo = models.CharField(max_length = 255)
    resumo = RichTextField(blank=True, null=True)
    conteudo = RichTextUploadingField()
    imagem_capa = models.ImageField(null= True, blank= True, upload_to="static/blog/")
    data_publicacao = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.titulo
    