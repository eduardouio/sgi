from django import forms


class FormAlmagro(forms.Form):
    """Formulario de importacion de formato CSV 
    """
    file = forms.FileField()