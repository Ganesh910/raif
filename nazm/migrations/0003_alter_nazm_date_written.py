# Generated by Django 4.1.5 on 2023-07-14 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nazm', '0002_nazm_date_written'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nazm',
            name='date_written',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 10, 43, 3, 173217, tzinfo=datetime.timezone.utc)),
        ),
    ]
