# Generated by Django 4.2.8 on 2025-02-26 10:42
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0013_document_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='template',
        ),
    ]
