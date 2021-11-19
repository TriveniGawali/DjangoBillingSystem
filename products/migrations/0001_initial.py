# Generated by Django 3.2.8 on 2021-11-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('product_sgst', models.CharField(max_length=30)),
                ('product_cgst', models.CharField(max_length=30)),
                ('product_igst', models.CharField(max_length=30)),
                ('product_desc', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]