from django import forms
from products.models import Product

all_products = ()
#all_products = (
#    (p.cod_contable,  p.nombre)
#    for p in Product.objects.all().order_by('nombre')
#)

deep_choices = (
    (0, 'Todos'),
    (10, 'Últimos 10'),
    (20, 'Últimos 20'),
    (50, 'Últimos 50'),
    (100, 'Últimos 100'),
)


class FormProductSeach(forms.Form):
    products = forms.ChoiceField(choices=all_products, widget=forms.Select(
        attrs={
            'class': 'form-control form-control-sm',
            'autofocus': 'true'
        }
    ))
    deep = forms.ChoiceField(
        choices=deep_choices,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-sm',
                'max-lenght': 3
            }
        )
    )
