# Generated by Django 5.1.6 on 2025-06-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_alter_slider_options_alter_slider_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(help_text='Upload slider image', upload_to='sliders/'),
        ),
    ]
