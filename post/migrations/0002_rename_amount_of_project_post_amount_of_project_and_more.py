# Generated by Django 4.0.5 on 2022-06-16 05:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='amount_Of_project',
            new_name='amount_of_project',
        ),
        migrations.RemoveField(
            model_name='post',
            name='completion_Date',
        ),
        migrations.AddField(
            model_name='post',
            name='completion_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
