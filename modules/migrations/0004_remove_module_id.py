# Generated by Django 5.1.1 on 2024-09-18 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_alter_module_date_created_alter_module_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='id',
        ),
    ]
