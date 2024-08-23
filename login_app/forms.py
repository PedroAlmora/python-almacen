from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission


class LoginForm(forms.Form):
   username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Usuario'}))
   password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Contraseña'}))


class CustomPasswordChangeForm(PasswordChangeForm):
   old_password = forms.CharField(
        label=_("Contraseña anterior"),
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Contraseña anterior'})
   )
   new_password1 = forms.CharField(
        label=_("Nueva contraseña"),
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Nueva contraseña'})
        help_text=_("La nueva contraseña debe contener al menos 12 caracteres, incluyendo números y caracteres especiales.")
   )
   new_password2 = forms.CharField(
        label=_("Confirmar nueva contraseña"),
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill', 'placeholder': 'Confirmar nueva contraseña'})
   )
   
class RegistroUsuarioForm(UserCreationForm):
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('visitante', 'Visitante'),
        ('almacenero', 'Almacenero'),
    )

    rol = forms.ChoiceField(choices=ROL_CHOICES, required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'rol', 'tarjeta_credito']