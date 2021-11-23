from django import forms

YEARS = (
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023')
)

MONTHS = (
    ('01', 'ENERO'),
    ('02', 'FEBRERO'),
    ('03', 'MARZO'),
    ('04', 'ABRIL'),
    ('05', 'MAYO'),
    ('06', 'JUNIO'),
    ('07', 'JULIO'),
    ('08', 'AGOSTO'),
    ('09', 'SEPTIEMBRE'),
    ('10', 'OCTUBRE'),
    ('11', 'NOVIEMBRE'),
    ('12', 'DICIEMBRE'),
    )


class FormICEXML(forms.Form):
    year = forms.ChoiceField(
        required=True,
        choices=YEARS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    month = forms.ChoiceField(
        choices=MONTHS,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sales = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2})
    )
    devs = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2} )
    )
    importations = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2})
    )
