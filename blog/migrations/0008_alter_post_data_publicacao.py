# Generated by Django 4.1.3 on 2022-11-29 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 29, 10, 57, 40, 791553, tzinfo=datetime.timezone.utc)),
        ),
    ]
