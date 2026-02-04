from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = [
            'id',
            'nombre',
            'fecha_nacimiento',
            'email',
            'telefono',
            'texto',
            'foto_perfil',
            'foto_resultado',
        ]

        widgets = {
            'id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Código alfanumérico'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email@correo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '55-2478-5578'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'foto_perfil': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'foto_resultado': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }

