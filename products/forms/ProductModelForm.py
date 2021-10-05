from products.models import Product
from django import forms


class ProductFormModel(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductFormModel, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Product
        fields = ('__all__')
        widgets = {
            'fecha_emision_registro': forms.DateInput(
                attrs={'type': 'date'}
                ),
            'fecha_vencimiento_registro': forms.DateInput(
                attrs={'type': 'date'}
                ),
            'id_producto': forms.HiddenInput()
        }
