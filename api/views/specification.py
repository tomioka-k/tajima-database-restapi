from django.db.models import Prefetch
from rest_framework import generics
from rest_framework import pagination
from django_filters import rest_framework as filters
from database.models.material import Material
from database.models.specification import Specification, SpecificationCompose, Walk
from database.models.document import SpecificationDocument
from api.serializers.database import SpecificationDocumentSerializer, SpecificationProcessSerializer, SpecificationSerializer, SpecificationDetailSerializer
from api.filters import SpecificationFilter


class CustomPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class SpecificationListAPIView(generics.ListAPIView):
    queryset = Specification.objects.select_related(
        'walk', 'method', 'part', 'method__category', 'paste'
    ).prefetch_related('base', 'paste').filter(is_display=True)
    serializer_class = SpecificationSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpecificationFilter


class SpecificationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Specification.objects.select_related().prefetch_related(
        Prefetch('process__material'), Prefetch(
            'process__material__category'), Prefetch('process__material__document')
    ).filter(is_display=True)
    serializer_class = SpecificationDetailSerializer
    lookup_field = 'slug'


class SpecificationDocumentListAPIView(generics.ListAPIView):
    serializer_class = SpecificationDocumentSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = SpecificationDocument.objects.filter(
            specification__slug=slug, is_display=True).select_related('category')
        return queryset


class SpecificationComposeListAPIView(generics.ListAPIView):
    serializer_class = SpecificationProcessSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        compose = SpecificationCompose.objects.filter(
            main_specification__slug=slug).values('sub_specification')
        queryset = Specification.objects.select_related().prefetch_related(
            Prefetch('process__material'), Prefetch(
                'process__material__category'), Prefetch('process__material__document')
        ).filter(id__in=compose)
        return queryset
