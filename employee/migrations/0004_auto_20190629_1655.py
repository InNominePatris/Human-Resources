# Generated by Django 2.0 on 2019-06-29 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20190629_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicstudies',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Description'),
        ),
    ]
