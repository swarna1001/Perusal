# Generated by Django 3.1 on 2021-03-06 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210305_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='genres',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
