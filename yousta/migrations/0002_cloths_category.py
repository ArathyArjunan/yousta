# Generated by Django 4.1.4 on 2023-10-14 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yousta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloths',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yousta.category'),
        ),
    ]
