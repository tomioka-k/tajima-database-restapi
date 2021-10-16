from django.db.models import query
from rest_framework import generics
from api.serializers.database import MethodSeriarizer, MethodCategorySerializer, BaseSerializer, PasteSerializer, WalkSerializer
from database.models.specification import Base, Method, MethodCategory, Paste, Walk


class MethodCategoryListAPIView(generics.ListAPIView):
    queryset = MethodCategory.objects.all()
    serializer_class = MethodCategorySerializer


class MethodListAPIView(generics.ListAPIView):
    queryset = Method.objects.all()
    serializer_class = MethodSeriarizer


class BaseListAPIView(generics.ListAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer


class PasteListAPIView(generics.ListAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer


class WalkListAPIView(generics.ListAPIView):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer
