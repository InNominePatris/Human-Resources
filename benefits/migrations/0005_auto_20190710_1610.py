# Generated by Django 2.0 on 2019-07-10 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20190710_1610'),
        ('benefits', '0004_auto_20190701_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthInsurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Name')),
                ('description', models.CharField(max_length=300, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Health insurance',
                'verbose_name_plural': 'Heath insurances',
            },
        ),
        migrations.CreateModel(
            name='HealthInsuranceApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10, verbose_name='Status')),
                ('provider', models.CharField(choices=[('Iniser', 'Iniser'), ('Assa', 'Assa'), ('América', 'America'), ('Inss', 'Inss')], max_length=14, verbose_name='Provider')),
                ('offer_date', models.DateField(verbose_name='Offer date')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee')),
                ('health_insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='benefits.HealthInsurance', verbose_name='Seguro médicco')),
            ],
            options={
                'verbose_name': 'Insurance application',
                'verbose_name_plural': 'Insurances application',
            },
        ),
        migrations.CreateModel(
            name='VacationPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateField(verbose_name='Initial date')),
                ('final_date', models.DateField(verbose_name='Final date')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10, verbose_name='Status')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('employee', models.ManyToManyField(to='employee.Employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Vacation plan',
                'verbose_name_plural': 'Vacations plan',
            },
        ),
        migrations.AlterModelOptions(
            name='vacationrequest',
            options={'verbose_name': 'Solicitud de vacaciones', 'verbose_name_plural': 'Solicitudes de vacaciones'},
        ),
        migrations.AlterField(
            model_name='vacationrequest',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
