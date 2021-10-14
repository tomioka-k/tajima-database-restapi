from django.db import models
from .specification import Specification
from django.contrib.auth import get_user_model
import datetime
import uuid

from ..function import validators


def specification_document_path(instance, filename):
    return 'database/specification/{}/{}/{}/{}_{}_{}.{}'.format(
        instance.specification, "document", instance.category, instance.category, instance.specification, datetime.date.today(), filename.split('.')[-1])


class SpecificationDocumentCategory(models.Model):
    id = models.CharField(primary_key=True, editable=True,
                          validators=[validators.alphanumeric], max_length=50)
    name = models.CharField(verbose_name="仕様書類カテゴリ名",
                            max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "仕様書類カテゴリ"
        verbose_name_plural = "仕様書類カテゴリ"


class SpecificationDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        SpecificationDocumentCategory, verbose_name="カテゴリ", on_delete=models.PROTECT)
    specification = models.ForeignKey(Specification, verbose_name="仕様",
                                      related_name="document", on_delete=models.PROTECT)
    name = models.CharField(verbose_name="名称", max_length=100)
    file = models.FileField(
        verbose_name="ファイル", upload_to=specification_document_path)
    is_display = models.BooleanField(
        verbose_name="公開",
        default=True,
        help_text="公開／非公開"
    )
    created_at = models.DateField(verbose_name="作成日", auto_now_add=True)
    updated_at = models.DateField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "仕様書類"
        verbose_name_plural = "仕様書類"
