from django.shortcuts import render

from django.contrib import messages

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from .models import CategoriaAc, AC

from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from .forms import ACForm

@login_required
def ac_ListView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    queryset = AC.objects.all()
    queryset = queryset.order_by("descricao")

    aluno = AC.objects.get(id = 1)
    total_horas = aluno.somar_total_horas_aluno(1)
    context = {
        "ac_list": queryset,
        "total_horas": total_horas
    }
    return render(request, "ac_list.html", context)

def categorias_ac_ListView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    queryset = CategoriaAc.objects.all()
    queryset = queryset.order_by("descricao")
    context = {
        "categorias_ac_list": queryset
    }
    return render(request, "categorias_ac.html", context)

@login_required
# Deve pegar o usuário e cadastrar
def ac_create_view(request):
    if request.method == "POST":
        form = ACForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            
            try:
                form.full_clean()
            except ValidationError as e:
                # Do something based on the errors contained in e.message_dict.
                # Display them to a user, or handle them programmatically.
                non_field_errors = e.message_dict[NON_FIELD_ERRORS]

            form.save()

            # redirect to a new URL:
            messages.success(request, 'AC Cadastrada com Sucesso.')
            return HttpResponseRedirect('/ac_list/')
            
        else:
            print(form.errors)
            messages.error(request, 'Algo deu errado. Tente novamente')
        
    form = ACForm()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        "form": form,
        "num_visits": num_visits
    }
    return render(request, "cadastro_ac.html", context)

