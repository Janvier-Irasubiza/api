# Generated by Django 5.1.6 on 2025-02-26 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_short_description_dining_short_desc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dining',
            old_name='name',
            new_name='title',
        ),
    ]
