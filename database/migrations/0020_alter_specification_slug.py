# Generated by Django 3.2.8 on 2021-10-16 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_specificationcompose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
