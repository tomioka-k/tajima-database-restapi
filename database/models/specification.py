from django.db import models
from django.contrib.auth import get_user_model
import datetime

from ..function import validators


def specification_image_path(instance, filename):
    return 'images/specification/{}/{}/{}.{}'.format(instance.id, "image", datetime.date.today(), filename.split('.')[-1])


def specification_interface_path(instance, filename):
    return 'images/specification/{}/{}/{}.{}'.format(instance.id, "interface", datetime.date.today(), filename.split('.')[-1])


def specification_cad_path(instance, filename):
    return 'images/specification/{}/{}/{}.{}'.format(instance.id, "cad", datetime.date.today(), filename.split('.')[-1])


class Category(models.Model):

    id = models.CharField(primary_key=True, editable=True,
                          validators=[validators.alphanumeric], max_length=50)
    name = models.CharField(
        verbose_name="カテゴリ",
        max_length=255,
        unique=True,
        help_text="防水材料のカテゴリ"
    )
    description = models.TextField(
        verbose_name="説明文",
        max_length=1000,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "カテゴリ"
        verbose_name_plural = "カテゴリ一覧"


class Base(models.Model):
    id = models.CharField(primary_key=True, editable=True,
                          validators=[validators.alphanumeric], max_length=50)
    name = models.CharField(verbose_name="下地", max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "下地"
        verbose_name_plural = "下地一覧"


class Slope(models.Model):
    id = models.CharField(primary_key=True, editable=True,
                          validators=[validators.alphanumeric], max_length=50)
    length = models.CharField(verbose_name="勾配", max_length=20)

    def __str__(self):
        return self.length

    class Meta:
        verbose_name = "勾配"
        verbose_name_plural = "勾配"


class Part(models.Model):
    id = models.CharField(primary_key=True, editable=True,
                          validators=[validators.alphanumeric], max_length=50)
    name = models.CharField(verbose_name="部位", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部位"
        verbose_name_plural = "部位一覧"


class Paste(models.Model):
    id = models.CharField(primary_key=True, editable=True,
                          validators=[validators.alphanumeric], max_length=50)
    name = models.CharField(verbose_name="貼り方", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "貼り方"
        verbose_name_plural = "貼り方"


class Walk(models.Model):
    id = models.CharField(primary_key=True, editable=True,
                          validators=[validators.alphanumeric], max_length=50)
    name = models.CharField(verbose_name="歩行用途", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "歩行用途"
        verbose_name_plural = "歩行用途"


class Specification(models.Model):
    """ 仕様 """
    id = models.CharField(primary_key=True, editable=True,
                          validators=[validators.alphanumeric], max_length=50)
    name = models.CharField(verbose_name="仕様名", max_length=255, unique=True)
    method_name = models.CharField(
        verbose_name="工法名", max_length=255, blank=True)
    description = models.CharField(
        verbose_name="説明文", max_length=255, blank=True)
    base = models.ManyToManyField(Base, verbose_name="適用下地")
    slope = models.ForeignKey(Slope, verbose_name="勾配",
                              on_delete=models.PROTECT)
    part = models.ForeignKey(Part, verbose_name="部位", on_delete=models.PROTECT)
    paste = models.ForeignKey(
        Paste, verbose_name="貼り方", on_delete=models.PROTECT)
    walk = models.ForeignKey(Walk, verbose_name="歩行用途",
                             on_delete=models.PROTECT)
    is_insulation = models.BooleanField(
        verbose_name="断熱",
        default=False,
        help_text="非断熱／断熱"
    )
    weight = models.FloatField(verbose_name="重量(kg/㎡)", blank=True, null=True)
    thickness = models.IntegerField(
        verbose_name="厚み/mm", blank=True, null=True)
    co2_usage = models.FloatField(
        verbose_name="CO2使用量(kg/㎡)", blank=True, null=True)
    service_life = models.IntegerField(
        verbose_name="耐用年数/年", blank=True, null=True)
    is_display = models.BooleanField(
        verbose_name="公開",
        default=True,
        help_text="公開／非公開"
    )
    remarks = models.TextField(verbose_name="備考", blank=True)
    image = models.ImageField(
        verbose_name="イメージ図", upload_to=specification_image_path, blank=True)
    interface = models.ImageField(
        verbose_name="納まり図", upload_to=specification_interface_path, blank=True)
    cad = models.ImageField(
        verbose_name="CAD図", upload_to=specification_cad_path, blank=True)
    created_at = models.DateField(verbose_name="作成日", auto_now_add=True)
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    creater = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "仕様"
        verbose_name_plural = "仕様一覧"
