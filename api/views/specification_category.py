from rest_framework import generics
from django_filters import rest_framework as filters
from api.serializers.database import MethodSeriarizer, MethodCategorySerializer, BaseSerializer, PasteSerializer, WalkSerializer
from database.models.specification import Base, Method, MethodCategory, Paste, Walk
from api.filters import MethodFilter, MethodCategoryFilter


class MethodCategoryListAPIView(generics.ListAPIView):
    queryset = MethodCategory.objects.all()
    serializer_class = MethodCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MethodCategoryFilter


class MethodListAPIView(generics.ListAPIView):
    queryset = Method.objects.all().select_related('category')
    serializer_class = MethodSeriarizer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MethodFilter


class MethodRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Method.objects.all().select_related('category')
    serializer_class = MethodSeriarizer
    lookup_field = 'slug'


class BaseListAPIView(generics.ListAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer


class PasteListAPIView(generics.ListAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer


class WalkListAPIView(generics.ListAPIView):
    queryset = Walk.objects.all()
    serializer_class = WalkSerializer
