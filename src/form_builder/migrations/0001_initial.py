# Generated by Django 4.1 on 2023-01-17 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_alter_product_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0, verbose_name='index')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('value', models.CharField(max_length=255, verbose_name='value')),
            ],
            options={
                'verbose_name': 'field option',
                'verbose_name_plural': 'field options',
            },
        ),
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='field_type_icons/%Y/%m/%d', verbose_name='icon')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='code')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'field type',
                'verbose_name_plural': 'field types',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('campaigns', models.ManyToManyField(blank=True, related_name='forms', to='app.campaign', verbose_name='campaigns')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forms', to=settings.AUTH_USER_MODEL)),
                ('employees', models.ManyToManyField(blank=True, related_name='employee_forms', to=settings.AUTH_USER_MODEL, verbose_name='employees')),
                ('plans', models.ManyToManyField(blank=True, related_name='forms', to='app.plan', verbose_name='plans')),
                ('stores', models.ManyToManyField(blank=True, related_name='forms', to='app.store', verbose_name='stores')),
            ],
            options={
                'verbose_name': 'form',
                'verbose_name_plural': 'forms',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='FormGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0, verbose_name='index')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_groups', to='form_builder.form')),
            ],
            options={
                'verbose_name': 'form group',
                'verbose_name_plural': 'form groups',
            },
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0, verbose_name='index')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('label', models.CharField(blank=True, max_length=255, null=True, verbose_name='label')),
                ('default_value', models.CharField(blank=True, max_length=255, null=True, verbose_name='default value')),
                ('use_default', models.BooleanField(default=False, verbose_name='use default')),
                ('required', models.BooleanField(default=False, verbose_name='required')),
                ('field_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='form_builder.fieldtype')),
                ('form_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='form_builder.formgroup')),
                ('options', models.ManyToManyField(blank=True, related_name='form_fields', to='form_builder.fieldoption')),
            ],
            options={
                'verbose_name': 'form field',
                'verbose_name_plural': 'form fields',
            },
        ),
    ]
