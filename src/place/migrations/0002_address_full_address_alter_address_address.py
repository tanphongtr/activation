# Generated by Django 4.1.4 on 2022-12-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='full_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='full address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=255, verbose_name='address'),
        ),
    ]
