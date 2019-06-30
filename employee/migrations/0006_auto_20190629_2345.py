# Generated by Django 2.0 on 2019-06-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20190629_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='type',
            field=models.CharField(choices=[('DNI', 'DNI'), ('PASSPORT', 'PASSPORT'), ('RESIDENCE', 'RESIDENCE')], default=True, max_length=10, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='type',
            field=models.CharField(choices=[('DNI', 'DNI'), ('PASSPORT', 'PASSPORT'), ('RESIDENCE', 'RESIDENCE')], default=True, max_length=10, verbose_name='Type'),
        ),
    ]
