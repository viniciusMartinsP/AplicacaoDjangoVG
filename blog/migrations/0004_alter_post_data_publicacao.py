# Generated by Django 4.1.3 on 2022-11-22 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 22, 1, 40, 36, 321361, tzinfo=datetime.timezone.utc)),
        ),
    ]
