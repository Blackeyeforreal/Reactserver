# Generated by Django 3.2.3 on 2021-05-31 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userdetails', '0004_auto_20210531_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email'),
        ),
    ]
