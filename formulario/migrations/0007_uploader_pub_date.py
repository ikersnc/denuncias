# Generated by Django 4.0.3 on 2022-03-11 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0006_remove_senya_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploader',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2022, 3, 11, 12, 30, 37, 500878, tzinfo=utc)),
        ),
    ]
