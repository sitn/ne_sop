# Generated by Django 4.2.8 on 2024-02-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0004_itemstatus_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='entitytype',
            name='service',
            field=models.BooleanField(default=False),
        ),
    ]
