# Generated by Django 5.1.6 on 2025-02-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_dining_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='dining',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
