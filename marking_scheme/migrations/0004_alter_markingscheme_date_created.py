# Generated by Django 5.1.1 on 2024-09-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking_scheme', '0003_remove_markingscheme_name_markingscheme_module_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markingscheme',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
