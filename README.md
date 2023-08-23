# trab3web2

Instruções para execução:

Como boa prática, recomenda-se a criação de um ambiente virtual (Utilizar o [venv](https://docs.python.org/pt-br/3/library/venv.html) , por exemplo):

```
python -m venv .
```

(Windows) Ativá-lo através do comando:

```
.\Scripts\Activate.ps1
```

Após clonar o projeto, acessar sua pasta raiz e fazer o download das dependências, com o seguinte comando:

```
pip install -r requirements.txt
```

Executar as migrations do BD:

```
python manage.py makemigrations
python manage.py migrate
```
Em seguida, criar um super usuário, com o seguinte comando (Rodar na pasta raiz do projeto, onde se encontra o manage.py):

```
python manage.py createsuperuser
```
Finalmente, executar o projeto:

```
python manage.py runserver
```
Para adicionar, editar ou excluir os models (Alunos, Disciplinas, Matrículas e Turmas), acessar o seguinte endereço:

http://127.0.0.1:8000/admin/

ou

http://localhost:8000/admin/

(Logar utilizando as credenciais do superuser criado anteriormente)

Para acessar o index:

http://127.0.0.1:8000/

ou

http://localhost:8000/
