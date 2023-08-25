from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


STATUS_CHOICES = (
    ('Aprovado', 'APROVADO'),
    ('Em Análise', 'EM ANÁLISE'),
    ('Recusado', 'RECUSADO'),
)

GENERO_CHOICES = (
    ('M', 'MASCULINO'),
    ('F', 'FEMININO'),
    ('Prefiro não informar', 'PREFIRO NÃO INFORMAR'),
)

# Create your models here.
class Pessoa(models.Model): # Classe Mãe
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=30) # Email institucional, ex:  lpds1@aluno.ifnmg.edu.br
    senha = models.CharField(max_length=20)
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES)
    # Etnia, Renda para gerar informações
    # Curso?

class Aluno(models.Model):
    # Especialização de Pessoa
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=30) # Email institucional, ex:  lpds1@aluno.ifnmg.edu.br
    senha = models.CharField(max_length=20)
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES)
    cod_matricula = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nome} '

class CategoriaAc(models.Model):
    # pk = ID
    descricao = models.CharField('Descrição', max_length=200)
    carga_horaria_maxima = models.IntegerField()

    def __str__(self):
        return f'{self.descricao}'
        
class AC(models.Model):
    # pk = ID
    categoria = models.ForeignKey(CategoriaAc, on_delete=models.PROTECT) # Relacionamento? 1 para 1
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT) # 1 para N
    carga_horaria = models.IntegerField("Carga Horária")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ANÁLISE") #choices  APROVADO, ANÁLISE, RECUSADO
    descricao = models.CharField("Descrição", max_length=200, default="")
    certificado = models.FileField(upload_to='static/certifications/') # Somente PDF

    def __str__(self):
        return f'AC: {self.categoria}, ALUNO: {self.aluno}, STATUS: {self.status} '
    
    def somar_total_horas_aluno(self, id):
        # List ACs
        ac_list = AC.objects.all()
        total_horas = 0
        for ac in ac_list:
            if ac.pk == id:
                total_horas += ac.carga_horaria
        return total_horas
    
    def somar_total_horas_categoria(self, categoria, id):
        ac_list = AC.objects.get(pk = id)
        total_horas_categoria = 0
        for ac in ac_list:
            if ac.categoria == categoria:
                total_horas_categoria += ac.carga_horaria
        return total_horas_categoria
    
    # Validação Limite Horas
    def clean_limite_horas(self):
        soma_horas_atuais_com_pretendidas = self.carga_horaria + self.somar_total_horas_categoria(categoria=self.categoria)

        # Caso o aluno já tenha o limite de horas naquela Categoria
        if self.carga_horaria == self.categoria.carga_horaria_maxima:
            raise ValidationError(
                ("Atenção! Você alcançou o limite de Horas para essa Categoria {}" .format(self.categoria.carga_horaria_maxima))
            )
        
        # Caso as Horas da nova atividade ultrapasse o limite
        elif soma_horas_atuais_com_pretendidas > self.categoria.carga_horaria_maxima:
            print("Atenção! Você alcançou o limite de Horas para essa Categoria {}" .format(self.categoria.carga_horaria_maxima))
            print("Serão aproveitadas apenas {} Horas" .format(self.categoria.carga_horaria_maxima - self.carga_horaria))
            soma_horas_atuais_com_pretendidas = self.categoria.carga_horaria_maxima

"""    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == "draft" and self.pub_date is not None:
            raise ValidationError(_("Draft entries may not have a publication date."))
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == "published" and self.pub_date is None:
            self.pub_date = datetime.date.today()
"""