# Generated by Django 2.0 on 2019-06-10 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0007_historicalemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', models.CharField(max_length=300, verbose_name='Explanation')),
                ('from_data', models.DateField(verbose_name='From data')),
                ('to_data', models.DateField(verbose_name='To data')),
                ('reason', models.CharField(max_length=20, verbose_name='Reason')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Attendance request',
                'verbose_name_plural': 'Attendances request',
            },
        ),
    ]
