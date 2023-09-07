from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

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

class UserManager(BaseUserManager):
    def create_user(self, login, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            login="test", password="123"
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    pass

    objects = UserManager()

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