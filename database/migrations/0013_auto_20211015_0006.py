# Generated by Django 3.2.8 on 2021-10-14 15:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20211014_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='method',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='工法名'),
        ),
        migrations.AlterField(
            model_name='methodcategory',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='カテゴリ名'),
        ),
        migrations.AlterField(
            model_name='specificationdocumentcategory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]