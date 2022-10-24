from django import forms
from django.forms import ModelForm
from .models import Persona, Localidad, Libro, Autor

# class ClienteForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=128)
#     edad = forms.IntegerField(label="Edad")
#     activo = forms.BooleanField(label="Activo", required=False)
#     TIPO_IVA_CHOICE = {
#         (1, "Resposable Inscripto"),
#         (2, "Monotributo"),
#         (3, "Exento")
#     }
#     tipo_iva = forms.ChoiceField(label="Tipo IVA", choices=TIPO_IVA_CHOICE)
#     fecha_nacimiento = forms.DateField(label="Fecha de nacimiento",
#                                        #input_formats=["%d/%m/%Y"],
#                                        widget=forms.DateInput(attrs={"type": "date"}))
        

class ClienteForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'