# Generated by Django 4.0 on 2022-01-08 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nsapp', '0002_instructor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.IntegerField(default=datetime.datetime(2022, 1, 8, 10, 14, 11, 537288, tzinfo=utc)),
            preserve_default=False,
        ),
    ]