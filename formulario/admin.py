from django.contrib import admin
from .models import Uploader, Denuncia

class UploaderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['aqui']}),
        ('Fecha de subida', {'fields': ['pub_date']}),
    ]

admin.site.register(Denuncia)
admin.site.register(Uploader, UploaderAdmin)
