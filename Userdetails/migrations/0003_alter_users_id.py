# Generated by Django 3.2.3 on 2021-05-30 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userdetails', '0002_auto_20210530_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
