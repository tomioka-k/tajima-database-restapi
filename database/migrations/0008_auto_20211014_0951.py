# Generated by Django 3.2.8 on 2021-10-14 00:51

import database.models.specification
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20211014_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='名称')),
                ('normalize_name', models.CharField(max_length=100, verbose_name='一般名称')),
                ('release_date', models.DateField(verbose_name='発売日')),
            ],
            options={
                'verbose_name': '工法',
                'verbose_name_plural': '工法',
            },
        ),
        migrations.CreateModel(
            name='MethodCategory',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '工法カテゴリ',
                'verbose_name_plural': '工法カテゴリ',
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterField(
            model_name='specification',
            name='cad',
            field=models.FileField(blank=True, upload_to=database.models.specification.specification_cad_path, verbose_name='CAD図'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='interface',
            field=models.FileField(blank=True, upload_to=database.models.specification.specification_interface_path, verbose_name='納まり図'),
        ),
        migrations.AlterField(
            model_name='specificationdocument',
            name='specification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='document', to='database.specification', verbose_name='仕様'),
        ),
        migrations.AddField(
            model_name='method',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.methodcategory', verbose_name='カテゴリ'),
        ),
        migrations.AddField(
            model_name='specification',
            name='method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='database.method', verbose_name='工法'),
            preserve_default=False,
        ),
    ]