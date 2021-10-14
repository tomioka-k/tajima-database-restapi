from django.db import models
from django.contrib.auth import get_user_model
import uuid
import datetime

from ..function import validators


def material_image_path(instance, filename):
    return 'database/material/{}/{}/{}_{}_{}.{}'.format(instance.name, "image", instance.name, "image", datetime.date.today(), filename.split('.')[-1])


def material_label_image_path(instance, filename):
    return 'database/material/{}/{}/{}_{}_{}.{}'.format(instance.name, "label_image", instance.name, "label_image", datetime.date.today(), filename.split('.')[-1])


def material_packing_image_path(instance, filename):
    return 'database/material/{}/{}/{}_{}_{}.{}'.format(instance.name, "packing_image", instance.name, "packing_image", datetime.date.today(), filename.split('.')[-1])


def material_cad_path(instance, filename):
    return 'database/material/{}/{}/{}_{}_{}.{}'.format(instance.name, "cad", instance.name, "cad", datetime.date.today(), filename.split('.')[-1])


class MaterialCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    name = models.CharField(
        verbose_name="材料種別",
        max_length=50,
        unique=True,
        help_text="例：シート類、プライマー"
    )
    order = models.IntegerField(verbose_name="並び順")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品カテゴリ"
        verbose_name_plural = "商品カテゴリ"


class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(
        MaterialCategory, verbose_name="カテゴリ", on_delete=models.PROTECT)
    name = models.CharField(verbose_name="商品名", max_length=100)
    normalize_name = models.CharField(
        verbose_name="一般名称",
        max_length=255,
        blank=True,
        help_text="例：アスファルト系プライマー"
    )
    standard = models.TextField(
        verbose_name="規格",
        max_length=255,
        help_text="例：1m × 8m"
    )
    remarks = models.TextField(verbose_name="備考", max_length=255, blank=True)
    description = models.TextField(
        verbose_name="説明文", max_length=255, blank=True)
    bto = models.BooleanField(verbose_name="受注生産品", default=False)
    material_image = models.ImageField(
        verbose_name="イメージ", upload_to=material_image_path, blank=True)
    label_image = models.ImageField(
        "ラベル", upload_to=material_label_image_path, blank=True)
    packing_image = models.ImageField(
        verbose_name="荷姿", upload_to=material_packing_image_path, blank=True)
    cad = models.FileField(
        verbose_name="CAD", upload_to=material_cad_path, blank=True)
    created_at = models.DateField(verbose_name="作成日", auto_now_add=True)
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"
