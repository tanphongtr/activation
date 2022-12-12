# Generated by Django 4.1.4 on 2022-12-11 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_plan_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('phone', models.CharField(max_length=255, verbose_name='phone')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('state', models.CharField(max_length=255, verbose_name='state')),
                ('country', models.CharField(max_length=255, verbose_name='country')),
                ('zip_code', models.CharField(max_length=255, verbose_name='zip code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('project', models.ManyToManyField(related_name='profiles', to='app.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
