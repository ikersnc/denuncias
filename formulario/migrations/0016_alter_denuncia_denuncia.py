# Generated by Django 4.0.3 on 2022-03-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0015_senya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='denuncia',
            field=models.FileField(blank=True, null=True, upload_to='aqui/'),
        ),
    ]