# Generated by Django 3.2.9 on 2022-01-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ram_app', '0004_auto_20220105_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_stone',
            name='path',
            field=models.CharField(default=235, max_length=300),
            preserve_default=False,
        ),
    ]