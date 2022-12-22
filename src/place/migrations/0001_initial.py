# Generated by Django 4.1 on 2022-12-15 14:36

import app.utils.generate
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='full address')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('code', models.CharField(blank=True, max_length=255, unique=True, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('code', models.CharField(blank=True, max_length=255, unique=True, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('code', models.CharField(blank=True, max_length=255, unique=True, verbose_name='code')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wards', to='place.district', to_field='code')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=app.utils.generate.nanoid_generate, max_length=255, unique=True, verbose_name='code')),
                ('lat', models.FloatField(verbose_name='latitude')),
                ('lng', models.FloatField(verbose_name='longitude')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='place.address')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='place.province', to_field='code'),
        ),
        migrations.AddField(
            model_name='address',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='place.ward', to_field='code'),
        ),
    ]
