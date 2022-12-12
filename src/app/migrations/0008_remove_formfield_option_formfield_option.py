# Generated by Django 4.1.4 on 2022-12-11 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_formfield_field_fieldoption_formfield_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='option',
        ),
        migrations.AddField(
            model_name='formfield',
            name='option',
            field=models.ManyToManyField(blank=True, related_name='form_fields', to='app.fieldoption'),
        ),
    ]
