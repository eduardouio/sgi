from django import forms


class FormICEXML(forms.Form):
    year = forms.IntegerField(required=True, widget=forms.NumberInput)
    month = forms.IntegerField(required=True, widget=forms.NumberInput)
    file = forms.FileField(required=True, widget=forms.FileInput)
