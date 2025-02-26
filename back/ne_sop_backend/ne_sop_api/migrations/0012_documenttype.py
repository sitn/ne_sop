# Generated by Django 4.2.8 on 2025-02-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ne_sop_api', '0011_rename_name_document_title_document_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
