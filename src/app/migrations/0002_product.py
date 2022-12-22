# Generated by Django 4.1 on 2022-12-21 19:38

import app.utils.generate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('code', models.CharField(blank=True, default=app.utils.generate.nanoid_generate, max_length=255, unique=True, verbose_name='code')),
                ('qty_remaining', models.IntegerField(default=0, verbose_name='qty remaining')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
            ],
            options={
                'verbose_name': 'plan',
                'verbose_name_plural': 'plans',
                'ordering': ('-created_at',),
            },
        ),
    ]
