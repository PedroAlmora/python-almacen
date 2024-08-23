from django import forms
from .models import *
import re

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    # def clean_precio(self):
    #     precio = self.cleaned_data.get('precio')
    #     if precio <= 0:
    #         raise forms.ValidationError("El precio debe ser mayor que cero.")
    #     return precio

    
    # def clean_nombre(self):
    #     nombre = self.cleaned_data.get('nombre')
    #     if not re.match(r'^[a-zA-Z\s]+$', nombre):
    #         raise forms.ValidationError("El nombre solo debe contener letras y espacios.")
    #     return nombre
    
    # def clean_codigo_barras(self):
    #     codigo_barras = self.cleaned_data.get('codigo_barras')
    #     if not re.match(r'^\d{8,12}$', codigo_barras):
    #         raise forms.ValidationError("El código de barras debe contener entre 8 y 12 dígitos.")
    #     return codigo_barras
    
class EscanearCodigoDeBarrasForm(forms.Form):
     codigo_barras = forms.CharField(label='Código de Barras', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 250px; margin: 0 auto;', 'id': 'id_codigo_barras'}))
     nombre_bulto = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 250px; margin: 0 auto;'}))

class EscanearCodigoDeBarrasDespachoForm(forms.Form):
     codigo_barras = forms.CharField(label='Código de Barras', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 250px; margin: 0 auto;', 'id': 'id_codigo_barras'}))
     nombre_despacho = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 250px; margin: 0 auto;'}))
     nombre_cliente = forms.CharField(label='Cliente', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 250px; margin: 0 auto;'}))

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['nombre', 'productos', 'estantes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['productos'].widget = forms.CheckboxSelectMultiple()
        self.fields['productos'].queryset = Producto.objects.all().order_by('codigo')

        self.fields['estantes'].widget = forms.CheckboxSelectMultiple()
        self.fields['estantes'].queryset = Estante.objects.all().order_by('nombre')
        
        
class EstanteForm(forms.ModelForm):
    class Meta:
        model = Estante
        fields = ['nombre', 'productos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['productos'].widget = forms.CheckboxSelectMultiple()
        self.fields['productos'].queryset = Producto.objects.all().order_by('codigo')
        
class CargarProductosForm(forms.Form):
    archivo_excel = forms.FileField(label='Archivo Excel')
    

class DespachoForm(forms.ModelForm):
    archivo_excel = forms.FileField(label='Archivo Excel', required=True, widget=forms.FileInput(attrs={'id': 'id_archivo_excel'}))

    class Meta:
        model = Despacho
        fields = ['nombre', 'cliente']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 250px; margin: 0 auto;'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control text-center', 'style': 'width: 250px; margin: 0 auto;'})
            
        }
        