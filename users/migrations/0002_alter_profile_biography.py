# Generated by Django 4.0.2 on 2022-04-06 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
