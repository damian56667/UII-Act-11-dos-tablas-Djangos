from django import forms
from .models import Marca, Producto

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre_marca', 'contacto_nombre', 'contacto_email', 'pais_origen', 'es_exclusiva']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio_venta', 'stock', 'id_marca', 'id_familia', 'foto']