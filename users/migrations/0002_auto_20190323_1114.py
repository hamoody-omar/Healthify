# Generated by Django 2.0.8 on 2019-03-23 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_provider',
            field=models.BooleanField(default=False),
        ),
    ]
