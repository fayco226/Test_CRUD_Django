# Generated by Django 5.0.1 on 2024-01-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_to_do_app', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]