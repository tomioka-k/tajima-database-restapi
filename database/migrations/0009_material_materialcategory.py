# Generated by Django 3.2.8 on 2021-10-14 02:10

import database.models.material
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20211014_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('normalize_name', models.CharField(blank=True, help_text='例：アスファルト系プライマー', max_length=255, verbose_name='一般名称')),
                ('standard', models.TextField(help_text='例：1m × 8m', max_length=255, verbose_name='規格')),
                ('remarks', models.TextField(blank=True, max_length=255, verbose_name='備考')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='説明文')),
                ('bto', models.BooleanField(default=False, verbose_name='受注生産品')),
                ('material_image', models.ImageField(blank=True, upload_to=database.models.material.material_image_path)),
                ('label_image', models.ImageField(blank=True, upload_to=database.models.material.material_label_image_path)),
                ('packing_image', models.ImageField(blank=True, upload_to=database.models.material.material_packing_image_path)),
                ('cad', models.FileField(blank=True, upload_to=database.models.material.material_cad_path)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='更新日')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='MaterialCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='例：シート類、プライマー', max_length=50, unique=True, verbose_name='材料種別')),
                ('order', models.IntegerField(verbose_name='並び順')),
            ],
            options={
                'verbose_name': '材料カテゴリ',
                'verbose_name_plural': '材料カテゴリ一覧',
            },
        ),
    ]
