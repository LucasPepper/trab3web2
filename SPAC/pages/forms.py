from django import forms

from .models import Aluno

from django.core.mail.message import EmailMessage

class ACForm(forms.Form):

    carga_horaria = forms.TimeField(label='Carga Horária')
    descricao = forms.CharField(label='Descrição', max_length=100, required=False)
    # certificado = forms.FileField(label='Certificado', widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # ClearableFileInput doesn't support uploading multiple files

def send_mail(self):
    nome = self.cleaned_data['nome']
    email = self.cleaned_data['email']
    assunto = self.cleaned_data['assunto']
    mensagem = self.cleaned_data['mensagem']

    conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
    mail = EmailMessage (
        subject='E-mail enviado pelo sistema Django',
        body = conteudo,
        from_email='pimentalucas@hotmail.com',
        to=['pimentalucas@hotmail.com', ],
        headers={'Reply.To':email},
    )
    print('send_mail')
    mail.send()