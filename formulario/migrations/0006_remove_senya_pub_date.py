# Generated by Django 4.0.3 on 2022-03-11 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0005_remove_denuncia_denuncia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senya',
            name='pub_date',
        ),
    ]