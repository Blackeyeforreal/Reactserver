# Generated by Django 3.2.3 on 2021-05-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userdetails', '0008_alter_users_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name'),
        ),
    ]
