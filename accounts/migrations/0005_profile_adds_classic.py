# Generated by Django 3.1 on 2021-02-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210218_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adds_classic',
            field=models.BooleanField(default=False, verbose_name='classic'),
        ),
    ]
