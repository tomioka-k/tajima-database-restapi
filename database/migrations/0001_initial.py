# Generated by Django 3.2.8 on 2021-10-13 14:48

import database.models.specification
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='下地')),
            ],
            options={
                'verbose_name': '下地',
                'verbose_name_plural': '下地一覧',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(help_text='防水材料のカテゴリ', max_length=255, unique=True, verbose_name='カテゴリ')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='説明文')),
            ],
            options={
                'verbose_name': 'カテゴリ',
                'verbose_name_plural': 'カテゴリ一覧',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=50, verbose_name='部位')),
            ],
            options={
                'verbose_name': '部位',
                'verbose_name_plural': '部位一覧',
            },
        ),
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=50, verbose_name='貼り方')),
            ],
            options={
                'verbose_name': '貼り方',
                'verbose_name_plural': '貼り方',
            },
        ),
        migrations.CreateModel(
            name='Slope',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('length', models.CharField(max_length=20, verbose_name='勾配')),
            ],
            options={
                'verbose_name': '勾配',
                'verbose_name_plural': '勾配',
            },
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=50, verbose_name='歩行用途')),
            ],
            options={
                'verbose_name': '歩行用途',
                'verbose_name_plural': '歩行用途',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='仕様名')),
                ('method_name', models.CharField(blank=True, max_length=255, verbose_name='工法名')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='説明文')),
                ('is_insulation', models.BooleanField(default=False, help_text='断熱／非断熱', verbose_name='断熱材')),
                ('is_display', models.BooleanField(default=True, help_text='公開／非公開', verbose_name='公開')),
                ('remarks', models.TextField(blank=True, verbose_name='備考')),
                ('image', models.ImageField(blank=True, upload_to=database.models.specification.specification_image_path, verbose_name='イメージ図')),
                ('interface', models.ImageField(blank=True, upload_to=database.models.specification.specification_interface_path, verbose_name='納まり図')),
                ('cad', models.ImageField(blank=True, upload_to=database.models.specification.specification_cad_path, verbose_name='CAD図')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='更新日')),
                ('base', models.ManyToManyField(to='database.Base', verbose_name='適用下地')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.part')),
                ('paste', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.paste')),
                ('slope', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.slope')),
                ('walk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.walk')),
            ],
            options={
                'verbose_name': '仕様',
                'verbose_name_plural': '仕様一覧',
            },
        ),
    ]
