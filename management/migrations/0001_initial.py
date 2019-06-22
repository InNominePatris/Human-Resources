# Generated by Django 2.0 on 2019-06-10 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0007_historicalemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('event_status', models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('Completed', 'Completed')], max_length=10, verbose_name='Event status')),
                ('training_program', models.CharField(max_length=30, verbose_name='Training program')),
                ('type', models.CharField(choices=[('Gaming', 'Gaming'), ('Online', 'Online'), ('Orientation', 'Orientation'), ('Coaching', 'Coaching'), ('Mvp', 'Mvp'), (('Workshop',), 'Workshop')], max_length=20, verbose_name='Type')),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Medium', 'Medium'), ('Expert', 'Expert')], max_length=20, verbose_name='Level')),
                ('start_time', models.DateField(verbose_name='Start time')),
                ('end_time', models.DateField(verbose_name='End time')),
                ('enterprise', models.CharField(max_length=30, verbose_name='Enterprise')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Training',
                'verbose_name_plural': 'Trainings',
            },
        ),
    ]
