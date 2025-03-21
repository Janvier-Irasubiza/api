# Generated by Django 5.1.6 on 2025-02-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_dining_options_dining_active_dining_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dining',
            name='category',
            field=models.CharField(blank=True, choices=[('african_dish', 'African Dish'), ('kinyarwanda_dish', 'Kinyarwanda Dish'), ('african_tradition', 'African Tradition')], default='kinyarwanda_dish', max_length=100, null=True, verbose_name='category'),
        ),
    ]
