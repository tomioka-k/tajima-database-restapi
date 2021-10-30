from django.db.models import fields
from django_filters import rest_framework as filters
from database.models.specification import Specification, MethodCategory, Method


class SpecificationFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Specification
        fields = ('method__category', 'method', 'name', 'base', 'part',
                  'paste', 'walk', 'is_insulation')


class MethodCategoryFilter(filters.FilterSet):
    class Meta:
        model = MethodCategory
        fields = ('slug', )


class MethodFilter(filters.FilterSet):
    class Meta:
        model = Method
        fields = ('category__slug',)
