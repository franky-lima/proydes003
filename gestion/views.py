from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import EntidadForm
from .models import Entidad

# Create your views here.

def entidad_list(request):
    entidades = Entidad.objects.order_by('ruc')
    return render(request, 'gestion/entidad_list.html', {'entidades': entidades})

def entidad_detail(request, pk):
    entidad = get_object_or_404(Entidad, pk=pk)
    return render(request, 'gestion/entidad_detail.html', {'entidad': entidad})

def entidad_new(request):
    if request.method == "POST":
        form = EntidadForm(request.POST) 
        if form.is_valid():
            entidad = form.save(commit=False) 
            entidad.save()
            return redirect('entidad_detail', pk=entidad.pk)
    else:
        form = EntidadForm()
    return render(request, 'gestion/entidad_edit.html', {'form': form})


def entidad_edit(request, pk):
    entidad = get_object_or_404(Entidad, pk=pk) 
    if request.method == "POST":
        form = EntidadForm(request.POST, instance=entidad) 
        if form.is_valid():
            entidad = form.save(commit=False)
            entidad.save()
            return redirect('entidad_detail', pk=entidad.pk)
    else:
        form = EntidadForm(instance=entidad)
    return render(request, 'gestion/entidad_edit.html', {'form': form})
            
