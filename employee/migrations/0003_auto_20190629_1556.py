# Generated by Django 2.0 on 2019-06-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190629_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=70, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='historicalemployee',
            name='email',
            field=models.EmailField(max_length=70, verbose_name='Email'),
        ),
    ]