from django.shortcuts import render

from django.contrib import messages

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from .models import CategoriaAc, AC

from .forms import ACForm

@login_required
def ac_ListView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    queryset = AC.objects.all()
    queryset = queryset.order_by("descricao")

    total_horas = 0

    for ac in queryset:
        total_horas += ac.carga_horaria

    progresso_horas = round( (total_horas / 120) * 100 , 1)
    if progresso_horas > 100:
        progresso_horas = 100


    context = {
        "ac_list": queryset,
        "total_horas": total_horas,
        "progresso_horas": progresso_horas

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
def ac_create_view(request):
    if request.method == "POST":
        form = ACForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
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

