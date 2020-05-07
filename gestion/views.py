from django.shortcuts import render, get_object_or_404
from .models import Entidad

# Create your views here.

def entidad_list(request):
    entidades = Entidad.objects.order_by('ruc')
    return render(request, 'gestion/entidad_list.html', {'entidades': entidades})

def entidad_detail(request, pk):
    entidad = get_object_or_404(Entidad, pk=pk)
    return render(request, 'gestion/entidad_detail.html', {'entidad': entidad})

# Create your views here.
