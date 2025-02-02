# Generated by Django 5.1.1 on 2024-09-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_id', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('region', models.CharField()),
                ('tsc_number', models.IntegerField()),
            ],
        ),
    ]
