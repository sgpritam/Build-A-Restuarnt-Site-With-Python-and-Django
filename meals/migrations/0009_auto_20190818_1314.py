# Generated by Django 2.2.4 on 2019-08-18 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0008_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
