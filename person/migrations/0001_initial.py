# Generated by Django 2.0 on 2019-06-29 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(max_length=20, verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last name')),
                ('gender', models.CharField(choices=[('f', 'Female'), ('m', 'Male')], max_length=1, verbose_name='Gender')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='Dni')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
    ]
