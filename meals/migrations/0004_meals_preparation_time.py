# Generated by Django 2.2.4 on 2019-08-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_remove_meals_preperation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='preparation_time',
            field=models.IntegerField(default=20, verbose_name=20),
            preserve_default=False,
        ),
    ]
