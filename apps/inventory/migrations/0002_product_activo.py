# Generated by Django 4.2.13 on 2024-05-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]