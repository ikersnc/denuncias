# Generated by Django 4.0.3 on 2022-03-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0011_alter_uploader_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploader',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
