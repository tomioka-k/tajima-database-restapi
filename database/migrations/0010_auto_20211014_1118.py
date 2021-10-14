# Generated by Django 3.2.8 on 2021-10-14 02:18

import database.models.material
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_material_materialcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='cad',
            field=models.FileField(blank=True, upload_to=database.models.material.material_cad_path, verbose_name='CAD'),
        ),
        migrations.AlterField(
            model_name='material',
            name='label_image',
            field=models.ImageField(blank=True, upload_to=database.models.material.material_label_image_path, verbose_name='ラベル'),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_image',
            field=models.ImageField(blank=True, upload_to=database.models.material.material_image_path, verbose_name='イメージ'),
        ),
        migrations.AlterField(
            model_name='material',
            name='packing_image',
            field=models.ImageField(blank=True, upload_to=database.models.material.material_packing_image_path, verbose_name='荷姿'),
        ),
        migrations.CreateModel(
            name='SpecificationLtinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(help_text='行程は1-20の間です', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='行程')),
                ('unit', models.IntegerField(blank=True, choices=[(0, '個'), (1, 'kg/㎡')], null=True, verbose_name='単位')),
                ('min_quantity', models.FloatField(blank=True, help_text='数量に幅が無い場合には最小数量を記入します', null=True, validators=[django.core.validators.MinValueValidator(0.001), django.core.validators.MaxValueValidator(1000.0)], verbose_name='最小数量')),
                ('max_quantity', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.001), django.core.validators.MaxValueValidator(1000.0)], verbose_name='最大数量')),
                ('remarks', models.CharField(blank=True, max_length=255, verbose_name='備考')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specificationltinerary', to='database.material', verbose_name='材料')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specificationltinerary', to='database.specification', verbose_name='仕様')),
            ],
            options={
                'verbose_name': '仕様工程',
                'verbose_name_plural': '仕様工程',
                'ordering': ('order',),
            },
        ),
    ]