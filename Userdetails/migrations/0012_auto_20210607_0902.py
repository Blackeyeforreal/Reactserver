# Generated by Django 3.2.3 on 2021-06-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userdetails', '0011_auto_20210606_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='sum',
        ),
        migrations.AddField(
            model_name='posts',
            name='summary',
            field=models.ImageField(blank=True, max_length=200, upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
