from django import forms

class UploadForm(forms.Form):
    docfile = forms.FileField(
        label='Selecciona un archivo'
    )
