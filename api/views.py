from rest_framework import generics
from database.models.specification import Specification, SpecificationCompose
from database.models.document import SpecificationDocument
from .serializers import SpecificationComposeSerializer, SpecificationDocumentSerializer, SpecificationSerializer, SpecificationDetailSerializer

# Create your views here.


class SpecificationListAPIView(generics.ListAPIView):
    queryset = Specification.objects.filter(is_display=True)
    serializer_class = SpecificationSerializer


class SpecificationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Specification.objects.filter(is_display=True).select_related()
    serializer_class = SpecificationDetailSerializer
    lookup_field = 'slug'


class SpecificationDocumentListAPIView(generics.ListAPIView):
    queryset = SpecificationDocument.objects.filter(is_display=True)
    serializer_class = SpecificationDocumentSerializer
    lookup_field = 'specification__slug'


class SpecificationComposeListAPIView(generics.ListAPIView):
    queryset = SpecificationCompose.objects.all()
    serializer_class = SpecificationComposeSerializer
    lookup_field = 'sub_specification__slug'
