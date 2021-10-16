from rest_framework import generics
from database.models.specification import Specification, SpecificationCompose
from database.models.document import SpecificationDocument
from .serializers import SpecificationComposeSerializer, SpecificationDocumentSerializer, SpecificationProcessSerializer, SpecificationSerializer, SpecificationDetailSerializer

# Create your views here.


class SpecificationListAPIView(generics.ListAPIView):
    queryset = Specification.objects.filter(is_display=True)
    serializer_class = SpecificationSerializer


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
    serializer_class = SpecificationDetailSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        compose = SpecificationCompose.objects.filter(
            main_specification__slug=slug).values('sub_specification')
        queryset = Specification.objects.filter(id__in=compose)
        return queryset
