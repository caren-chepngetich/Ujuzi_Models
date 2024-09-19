# Generated by Django 5.1.1 on 2024-09-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KICD', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kicd',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='kicd',
            name='id',
        ),
        migrations.AddField(
            model_name='kicd',
            name='last_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kicd',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='kicd',
            name='kicd_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
