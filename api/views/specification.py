from rest_framework import generics
from rest_framework import pagination
from django_filters import rest_framework as filters
from database.models.specification import Specification, SpecificationCompose
from database.models.document import SpecificationDocument
from api.serializers.database import SpecificationDocumentSerializer, SpecificationProcessSerializer, SpecificationSerializer, SpecificationDetailSerializer
from api.filters import SpecificationFilter


class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class SpecificationListAPIView(generics.ListAPIView):
    queryset = Specification.objects.filter(is_display=True)
    serializer_class = SpecificationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpecificationFilter


class SpecificationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Specification.objects.filter(is_display=True).select_related()
    serializer_class = SpecificationDetailSerializer
    lookup_field = 'slug'


class SpecificationDocumentListAPIView(generics.ListAPIView):
    serializer_class = SpecificationDocumentSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = SpecificationDocument.objects.filter(
            specification__slug=slug, is_display=True)
        return queryset


class SpecificationComposeListAPIView(generics.ListAPIView):
    serializer_class = SpecificationProcessSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        compose = SpecificationCompose.objects.filter(
            main_specification__slug=slug).values('sub_specification')
        queryset = Specification.objects.filter(id__in=compose)
        return queryset
