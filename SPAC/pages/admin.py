from django.contrib import admin
from .models import Aluno, Coordenador, CategoriaAc, AC

# Register your models here.

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('Aluno', 'Coordenador', 'CategoriaAC', 'AC')

admin.site.register(Aluno)
admin.site.register(Coordenador)
admin.site.register(CategoriaAc)
admin.site.register(AC)