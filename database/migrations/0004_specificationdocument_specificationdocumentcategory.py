# Generated by Django 3.2.8 on 2021-10-13 16:28

import database.models.document
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20211014_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecificationDocumentCategory',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='仕様書類カテゴリ名')),
            ],
            options={
                'verbose_name': '仕様書類カテゴリ',
                'verbose_name_plural': '仕様書類カテゴリ',
            },
        ),
        migrations.CreateModel(
            name='SpecificationDocument',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('file', models.ImageField(upload_to=database.models.document.specification_document_path, verbose_name='ファイル')),
                ('is_display', models.BooleanField(default=True, help_text='公開／非公開', verbose_name='公開')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specification_document', to='database.specification', verbose_name='仕様')),
            ],
        ),
    ]
