# Generated by Django 4.2.3 on 2023-07-29 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='updated_ap',
            new_name='updated_ad',
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]
