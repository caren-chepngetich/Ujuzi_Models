# Generated by Django 5.1.1 on 2024-09-18 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0003_alter_assessment_assessment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='assessment_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessment_duration',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
