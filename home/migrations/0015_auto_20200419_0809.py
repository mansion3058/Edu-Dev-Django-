# Generated by Django 3.0.4 on 2020-04-19 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200418_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name_plural': 'Coming Events'},
        ),
        migrations.AlterModelOptions(
            name='headlines',
            options={'verbose_name_plural': 'Headlines'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name_plural': 'Subscribers'},
        ),
    ]
