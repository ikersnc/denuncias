from django.contrib import admin
from .models import Uploader

class UploaderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['aqui']}),
        ('Fecha de subida', {'fields': ['pub_date']}),
    ]

admin.site.register(Uploader, UploaderAdmin)
