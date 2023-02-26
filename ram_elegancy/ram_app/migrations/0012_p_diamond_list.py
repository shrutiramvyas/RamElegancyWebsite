# Generated by Django 3.2.8 on 2022-04-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ram_app', '0011_auto_20220331_0254'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_diamond_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diamond_name', models.CharField(max_length=30)),
                ('image', models.ImageField(default='', upload_to='diamond_images')),
                ('d_color', models.CharField(max_length=30)),
                ('d_clearity', models.CharField(max_length=20)),
                ('d_shape', models.CharField(max_length=20)),
                ('d_carat', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('d_desc', models.CharField(max_length=30)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]