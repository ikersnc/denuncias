# Generated by Django 4.0.3 on 2022-03-11 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_rename_uploadpdf_uploader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Senya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senya', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='formulario.uploader')),
            ],
        ),
    ]