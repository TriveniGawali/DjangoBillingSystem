# Generated by Django 3.2.8 on 2021-11-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
    ]
