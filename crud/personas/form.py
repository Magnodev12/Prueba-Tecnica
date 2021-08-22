from django.forms import ModelForm, fields
from .models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'



