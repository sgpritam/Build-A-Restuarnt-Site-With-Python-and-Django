# Generated by Django 2.2.4 on 2019-08-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meals',
            old_name='peoplr',
            new_name='people',
        ),
        migrations.AddField(
            model_name='meals',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meals',
            name='preperation_time',
            field=models.IntegerField(),
        ),
    ]
