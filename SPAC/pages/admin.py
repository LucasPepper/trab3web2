from django.contrib import admin
from .models import Aluno, CategoriaAc, AC

# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ('Aluno', 'CategoriaAC', 'AC')

admin.site.register(Aluno)
admin.site.register(CategoriaAc)
admin.site.register(AC)