# Generated by Django 2.0 on 2019-07-10 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charge',
            name='payment',
        ),
    ]
