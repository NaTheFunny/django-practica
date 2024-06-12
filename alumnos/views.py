from django.shortcuts import render
from .models import Alumno, Genero
# Create your views here.

def index(request):
    context={}
    return render(request,'alumnos/index.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)