# Generated by Django 3.1 on 2021-02-23 09:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210223_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='DEFAULT VALUE', editable=False, populate_from='user'),
        ),
    ]
