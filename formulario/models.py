from django.db import models
from django import forms
from django.utils import timezone
#comentario para ver si acode funciona
class Denuncia(models.Model):
    #denuncia = models.FileField(upload_to = 'aqui/', blank = True, null = True)
    denuncia = models.CharField(max_length=200, null = True)
    def __str__(self, denuncia):
        self.denuncia = denuncia
        return self.denuncia

class Uploader(models.Model):
    aqui = models.FileField(upload_to = 'aqui/', blank = True, null = True)
    pub_date = models.DateTimeField(null = True)

class Senya(models.Model):
    senya = models.ForeignKey(Uploader, on_delete = models.RESTRICT)
