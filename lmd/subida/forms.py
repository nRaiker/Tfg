from django import forms

class UploadForm(forms.Form):
    docfile = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'filestyle','data-buttonText':'Selecciona un archivo',"data-buttonName":"btn-primary"}
        )
        ,label='Selecciona un archivo'
    )
