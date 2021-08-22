from django.shortcuts import render , get_object_or_404, redirect
from .models import Persona
from .form import PersonaForm

def inicio(request):
    personass = Persona.objects.all()
    context = {
        'personass' : personass
    }
    return render(request,'personas/inicio.html', context)

def detail(request , id) :
    persona = get_object_or_404(Persona , pk = id) 

    return render(
        request , 'personas/detail.html' ,
        {
            'Persona' : Persona
        }
    )

def crear_persona(request) :
    if request.method == "POST" :
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid() :
            persona_form.save()
            return redirect('inicio')
    else :
        persona_form = PersonaForm()

    return render(
        request , 'personas/crear.html' ,
        {
            'persona_form' : persona_form
        }
    )


def actualizar_persona(request , id) :
    persona = get_object_or_404(Persona , pk = id)

    if request.method == "POST" :
        persona_form = PersonaForm(request.POST , instance = persona) 
        if persona_form.is_valid() :
            persona_form.save()
            return redirect('inicio')
    else :
        persona_form = PersonaForm(instance = persona)

    return render(
        request , 'personas/editar.html' ,
        {
            'persona_form' : persona_form
        }
    )


def borrar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if persona:
        persona.delete()
        return redirect('inicio')

# Create your views here.
