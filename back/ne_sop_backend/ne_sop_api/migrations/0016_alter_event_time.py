# Generated by Django 5.0 on 2023-12-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0015_rename_content_item_description_alter_item_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]
