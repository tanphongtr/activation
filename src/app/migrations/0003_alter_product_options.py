# Generated by Django 4.1 on 2023-01-17 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
