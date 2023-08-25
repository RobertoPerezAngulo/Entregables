from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Persona

# Create your views here.
def index(request):
    metodoPersona()
    return HttpResponse("Hola Mundo desde Django")

def metodoPersona():
    persona = Persona(nombre='Juan', apellido='Perez chosto', edad=20, telefono='12345678')
    persona.save()
    print(persona.__str__())