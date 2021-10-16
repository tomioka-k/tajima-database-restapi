from django_filters import rest_framework as filters
from database.models.specification import Specification


class SpecificationFilter(filters.FilterSet):

    class Meta:
        model = Specification
        fields = ('method__category', 'method', 'name', 'base', 'part',
                  'paste', 'walk', 'is_insulation')
