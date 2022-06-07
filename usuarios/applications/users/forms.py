from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    """Formulario para la creacion de un usuario"""

    password1 = forms.CharField(
        label='Contraseña',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'********'
            }
        )
    )
    password2 = forms.CharField(
        label='Repetir contraseña',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'********'
            }
        )
    )
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    def clean_password2(self):
        """verificar si ambas contraseñas coinciden"""
        password1= self.cleaned_data['password1']
        password2= self.cleaned_data['password2']

        if password1 != password2:            
            self.add_error('password2', 'Las contraseñas no coinciden')

        if len(password1) < 8:
            self.add_error('password1', 'La contraseña debe contener mínimo 8 carácteres')
    
class LoginForm(forms.Form):
    """Formulario para el login"""

    username = forms.CharField(
        label='Nombre de usuario',
        required= True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username'
            }
        )
    )    
    password = forms.CharField(
        label='Contraseña',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    def clean(self):
        """validacion de datos de usuario"""
        cleaned_data= super(LoginForm, self).clean()
        username= self.cleaned_data['username']
        password= self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('No pudimos verificar tu cuenta con esa información.')
        return self.cleaned_data

class ChangePasswordForm(forms.Form):    
    password1 = forms.CharField(
        label='Contraseña',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña nueva',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña nueva'
            }
        )
    )