# Generated by Django 3.2.6 on 2022-01-13 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ram_app', '0008_auto_20220111_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sp_stone',
            old_name='name',
            new_name='sp_name',
        ),
    ]
