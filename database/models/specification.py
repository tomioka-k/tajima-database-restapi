from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
import uuid

from .material import Material
from ..function import validators


def specification_image_path(instance, filename):
    return 'database/specification/{}/{}/{}_{}_{}.{}'.format(instance.name, "image", instance.name, "image", datetime.date.today(), filename.split('.')[-1])


def specification_interface_path(instance, filename):
    return 'database/specification/{}/{}/{}_{}_{}.{}'.format(instance.name, "interface", instance.name, "interface", datetime.date.today(), filename.split('.')[-1])


def specification_cad_path(instance, filename):
    return 'database/specification/{}/{}/{}_{}_{}.{}'.format(instance.name, "cad", instance.name, "cad", datetime.date.today(), filename.split('.')[-1])


class MethodCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    name = models.CharField(verbose_name="カテゴリ名", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工法カテゴリ"
        verbose_name_plural = "工法カテゴリ"


class Method(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(
        MethodCategory, verbose_name="カテゴリ", on_delete=models.PROTECT)
    name = models.CharField(verbose_name="工法名", max_length=50, unique=True)
    normalize_name = models.CharField(verbose_name="一般名称", max_length=100)
    release_date = models.DateField(verbose_name="発売日")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工法"
        verbose_name_plural = "工法"


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="下地", max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "下地"
        verbose_name_plural = "下地一覧"


class Slope(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    length = models.CharField(verbose_name="勾配", max_length=20)

    def __str__(self):
        return self.length

    class Meta:
        verbose_name = "勾配"
        verbose_name_plural = "勾配"


class Part(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="部位", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部位"
        verbose_name_plural = "部位一覧"


class Paste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="貼り方", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "貼り方"
        verbose_name_plural = "貼り方"


class Walk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="歩行用途", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "歩行用途"
        verbose_name_plural = "歩行用途"


class Specification(models.Model):
    """ 仕様 """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    name = models.CharField(verbose_name="仕様名", max_length=255, unique=True)
    method = models.ForeignKey(
        Method, verbose_name="工法", on_delete=models.PROTECT)
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
    interface = models.FileField(
        verbose_name="納まり図", upload_to=specification_interface_path, blank=True)
    cad = models.FileField(
        verbose_name="CAD図", upload_to=specification_cad_path, blank=True)
    created_at = models.DateField(verbose_name="作成日", auto_now_add=True)
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    creater = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "仕様"
        verbose_name_plural = "仕様一覧"


class SpecificationProcess(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    specification = models.ForeignKey(
        Specification,
        verbose_name="仕様",
        related_name='process',
        on_delete=models.PROTECT
    )
    order = models.IntegerField(
        verbose_name="行程",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ],
        help_text="行程は1-20の間です"
    )
    material = models.ForeignKey(
        Material,
        verbose_name="材料",
        related_name="process",
        on_delete=models.PROTECT
    )
    unit = models.IntegerField(
        verbose_name="単位",
        choices=(
            (0, "個"),
            (1, "kg/㎡")
        ),
        blank=True,
        null=True
    )
    min_quantity = models.FloatField(
        verbose_name="最小数量",
        help_text="数量に幅が無い場合には最小数量を記入します",
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0.001),
            MaxValueValidator(1000.000)
        ]
    )
    max_quantity = models.FloatField(
        verbose_name="最大数量",
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0.001),
            MaxValueValidator(1000.000)
        ]
    )
    remarks = models.CharField(verbose_name="備考", max_length=255, blank=True)

    def __str__(self):
        return "{}_{}_{}".format(self.order, self.material.name, self.specification)

    class Meta:
        verbose_name = "仕様工程"
        verbose_name_plural = "仕様工程"
        ordering = ('order', )
