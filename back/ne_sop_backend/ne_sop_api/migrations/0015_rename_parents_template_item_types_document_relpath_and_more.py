# Generated by Django 4.2.7 on 2023-12-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0014_item_oralresponse_item_writtenresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='parents',
            new_name='item_types',
        ),
        migrations.AddField(
            model_name='document',
            name='relpath',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='document',
            name='version',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='template',
            name='relpath',
            field=models.CharField(default=None, max_length=400),
        ),
    ]
