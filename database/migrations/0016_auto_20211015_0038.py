# Generated by Django 3.2.8 on 2021-10-14 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_specificationdocument_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialcategory',
            options={'verbose_name': '商品カテゴリ', 'verbose_name_plural': '商品カテゴリ'},
        ),
        migrations.AddField(
            model_name='material',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='database.materialcategory', verbose_name='カテゴリ'),
        ),
    ]
