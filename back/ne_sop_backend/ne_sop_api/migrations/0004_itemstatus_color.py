# Generated by Django 4.2.7 on 2023-11-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0003_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemstatus',
            name='color',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]