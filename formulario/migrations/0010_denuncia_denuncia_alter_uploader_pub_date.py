# Generated by Django 4.0.3 on 2022-03-14 08:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0009_uploader_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='denuncia',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='uploader',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2022, 3, 14, 8, 50, 30, 711751, tzinfo=utc)),
        ),
    ]