from django.db import models
import uuid

from ..function import validators


def specification_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/images/specification/<filename>
    return 'images/specification/{}/{}.{}'.format(instance.id, str(uuid.uuid4()), filename.split('.')[-1])


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
    part = models.IntegerField(
        verbose_name="適用部位",
        choices=(
            (0, '平場'),
            (1, '立上り'),
        )
    )
    how_to_paste = models.IntegerField(
        verbose_name="密着/絶縁",
        choices=(
            (0, '密着'),
            (1, '絶縁')
        )
    )
    walk = models.IntegerField(
        verbose_name="歩行用途",
        choices=(
            (0, '非歩行'),
            (1, '軽歩行'),
            (2, '歩行')
        )
    )
    insulation = models.IntegerField(
        verbose_name="非断熱/断熱",
        choices=(
            (0, "非断熱"),
            (1, "断熱")
        )
    )
    is_display = models.BooleanField(
        verbose_name="表示",
        default=True,
        help_text="公開／非公開"
    )
    remarks = models.TextField(verbose_name="備考", blank=True)
    image1 = models.ImageField(
        upload_to=specification_directory_path, blank=True)
    image2 = models.ImageField(
        upload_to=specification_directory_path, blank=True)
    image3 = models.ImageField(
        upload_to=specification_directory_path, blank=True)
    created_at = models.DateField(verbose_name="作成日", auto_now_add=True)
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "仕様"
        verbose_name_plural = "仕様一覧"
