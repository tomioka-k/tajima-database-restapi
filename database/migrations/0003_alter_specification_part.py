# Generated by Django 3.2.8 on 2021-10-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20211013_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='part',
            field=models.IntegerField(choices=[(0, '平場'), (1, '立上り')], verbose_name='適用部位'),
        ),
    ]