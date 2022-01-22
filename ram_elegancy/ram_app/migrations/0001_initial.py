# Generated by Django 3.2.8 on 2021-11-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('stone_name', models.CharField(max_length=30)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('stone_color', models.CharField(max_length=30)),
                ('stone_clearity', models.CharField(max_length=20)),
                ('stone_cut', models.CharField(max_length=20)),
                ('stone_carat_size', models.CharField(max_length=20)),
                ('stone_inclusion', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
