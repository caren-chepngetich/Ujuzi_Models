# Generated by Django 5.1.1 on 2024-09-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KICD', '0003_alter_kicd_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='kicd',
            name='teacher_id',
            field=models.IntegerField(default=1),
        ),
    ]