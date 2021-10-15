# Generated by Django 3.2.8 on 2021-10-15 17:17

import database.models.document
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_alter_material_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialDocumentCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='商品書類カテゴリ名')),
            ],
            options={
                'verbose_name': '商品書類カテゴリ',
                'verbose_name_plural': '商品書類カテゴリ',
            },
        ),
        migrations.CreateModel(
            name='MaterialDocument',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('file', models.FileField(upload_to=database.models.document.material_document_path, verbose_name='ファイル')),
                ('is_display', models.BooleanField(default=True, help_text='公開／非公開', verbose_name='公開')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='更新日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.materialdocumentcategory', verbose_name='カテゴリ')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='document', to='database.material', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品書類',
                'verbose_name_plural': '商品書類',
            },
        ),
    ]
