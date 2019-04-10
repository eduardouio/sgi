from django import forms
from filemanager.models import FileManager

class FileUploadModelForm(forms.Form):
    TYPE = (
        (None, 'Seleccione...'),
        ('LIQUIDACION TRIBUTOS', 'LIQUIDACION TRIBUTOS'),
        ('LIQUIDACION ETIQUETAS', 'LIQUIDACION ETIQUETAS'),
        ('DAI', 'DAI'),
    )
    url = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control form-control-sm','autofocus':'autofocus'}))
    tipo = forms.ChoiceField(choices=TYPE, widget=forms.Select(attrs={'class':'form-control form-control-sm'}))
    pedido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    parcial = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
