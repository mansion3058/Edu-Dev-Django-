# Generated by Django 3.0.4 on 2020-04-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200417_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='headlines',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
