# Generated by Django 5.1.1 on 2024-09-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0002_remove_assessment_date_created_remove_assessment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='assessment_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='kicd_id',
            field=models.IntegerField(default=1),
        ),
    ]
