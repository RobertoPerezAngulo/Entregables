# Generated by Django 4.2.4 on 2023-08-25 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='email',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fecha_nacimiento',
        ),
    ]