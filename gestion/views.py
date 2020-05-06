from django.shortcuts import render, get_object_or_404
from .models import entidad

# Create your views here.

def entidad_list(request):
    entidades = entidad.objects.order_by('ruc')
    return render(request, 'gestion/entidad_list.html', {'entidades': entidades})


# Create your views here.
