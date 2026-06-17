from django.shortcuts import render, redirect
from phoneapp.models import Smartphone
from phoneapp.forms import SmartphoneForm, ManufacturerForm


def lista_smartphones(request):
    smartphones = Smartphone.objects.select_related('manufacturer').all().order_by('manufacturer__name')
    return render(request, 'phoneapp/lista_smartphones.html', {'smartphones': smartphones, 'titulo': 'Catálogo de Smartphones'})


def crear_smartphone(request):
    if request.method == 'POST':
        form = SmartphoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_smartphones')
    else:
        form = SmartphoneForm()

    return render(request, 'phoneapp/formulario.html', { 'form': form, 'titulo': 'Crear smartphone'})
