# Generated by Django 2.0 on 2019-07-17 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benefits', '0006_remove_healthinsuranceapplication_offer_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacationplan',
            options={'verbose_name': 'Plan de vacaciones', 'verbose_name_plural': 'Planes de vacaciones'},
        ),
    ]
