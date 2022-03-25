from django import forms
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Uploader, Denuncia
from django.forms import ClearableFileInput

class Texto(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['denuncia']
        value = Denuncia()
        widgets = {
            'denuncia':forms.Textarea(attrs = {'placeholder':'Explica aquí tu denuncia'})
        }

class UploadedFiles(forms.ModelForm):
    #img = forms.ImageField(label = 'Imágenes', required = False)
    class Meta:
        model = Uploader
        fields = ['aqui']
        widgets = {
            'aqui':ClearableFileInput(attrs = {'multiple':True}),
        }
    #arch = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple':True}), label = 'Archivo', required = False)