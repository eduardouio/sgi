from django import forms
from products.models import Product

all_products = (
    (p.cod_contable,  p.nombre)
    for p in Product.objects.all().order_by('nombre')
)


class FormProductSeach(forms.Form):
    products = forms.ChoiceField(choices=all_products)
