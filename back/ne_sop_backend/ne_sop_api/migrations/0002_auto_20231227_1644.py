# Generated by Django 4.2.8 on 2023-12-20 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ne_sop_api", "0001_initial"),
    ]

    def apply_migration(apps, schema_editor):
        Group = apps.get_model('auth', 'Group')
        Group.objects.bulk_create([
            Group(name=u'Manager'),
        ])


    def revert_migration(apps, schema_editor):
        Group = apps.get_model('auth', 'Group')
        Group.objects.filter(
            name__in=[
                u'Manager',
            ]
        ).delete()

    operations = [
        migrations.RunPython(apply_migration, revert_migration)
    ]
