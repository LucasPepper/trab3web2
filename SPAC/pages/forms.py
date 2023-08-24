from django import forms

from .models import AC

class ACForm(forms.ModelForm):
    class Meta:
        model = AC
        fields = [
            'categoria',
            'aluno',
            'carga_horaria',
            'descricao',
            'certificado'
        ]