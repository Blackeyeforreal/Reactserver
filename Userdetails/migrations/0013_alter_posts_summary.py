# Generated by Django 3.2.3 on 2021-06-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userdetails', '0012_auto_20210607_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='summary',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
