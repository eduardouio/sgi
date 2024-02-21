from django import forms
from orders.models import Order


class OrderFormModel(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderFormModel, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Order
        fields = ("__all__")
        widgets = {
            'fecha_embarque': forms.DateInput(attrs={'type': 'date'}),
            'fecha_arribo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida_bodega_puerto': forms.DateInput(attrs={'type': 'date'}),
            'fecha_ingreso_almacenera': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida_almacenera': forms.DateInput(attrs={'type': 'date'}),
            'fecha_liquidacion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_llegada_cliente': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida_autorizada_puerto': forms.DateInput(attrs={'type': 'date'}),
            'fecha_cierre': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida_origen': forms.DateInput(attrs={'type': 'date'}),
            'fecha_declaracion_inicial': forms.DateInput(attrs={'type': 'date'}),
            'fecha_ingreso_puerta': forms.DateInput(attrs={'type': 'date'}),
            'fecha_movilizacion_contenedor': forms.DateInput(attrs={'type': 'date'}),
            'fecha_envio_documentos': forms.DateInput(attrs={'type': 'date'}),
            'fecha_entrega_etiquetas_senae': forms.DateInput(attrs={'type': 'date'}),
            'fecha_pegado_etiquetas': forms.DateInput(attrs={'type': 'date'}),
            'fecha_aforo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_envio_de_documentos': forms.DateInput(attrs={'type': 'date'}),
            'fecha_aprovacion_compra': forms.DateInput(attrs={'type': 'date'}),
            'fecha_llegada_documentos': forms.DateInput(attrs={'type': 'date'}),
            'fecha_aprovacion_dai': forms.DateInput(attrs={'type': 'date'}),
            'fecha_emision_bl': forms.DateInput(attrs={'type': 'date'}),
            'id_pedido': forms.HiddenInput()
        }
