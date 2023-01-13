from django.contrib import admin

from .models import Alternativa, Questao


#Fazendo com que os objetos sejam exibidos juntos na tela de ADMIN
class AlternativaInline(admin.TabularInline):
    model = Alternativa

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AlternativaInline
    ]
    class Meta:
        model = Questao


admin.site.register(Questao, QuestionAdmin)
admin.site.register(Alternativa)