# Generated by Django 3.2.8 on 2021-10-14 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20211015_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.materialcategory', verbose_name='カテゴリ'),
        ),
    ]
