from django.shortcuts import render

from .models import CategoriaAc

# from .forms import FileFieldForm

# Create your views here.

def categorias_ac_ListView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    queryset = CategoriaAc.objects.all()
    queryset = queryset.order_by("descricao")
    context = {
        "categorias_ac_list": queryset
    }
    return render(request, "categorias_ac.html", context)

# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'upload.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

def cadastro_ac(request):
    return render(request, 'cadastro_ac.html')