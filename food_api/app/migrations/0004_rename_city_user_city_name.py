# Generated by Django 5.0.2 on 2024-03-13 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_foodproduct_fvrt_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city',
            new_name='city_name',
        ),
    ]
