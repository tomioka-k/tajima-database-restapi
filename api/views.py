from rest_framework import generics
from database.models.specification import Specification
from .serializers import SpecificationSerializer, SpecificationDetailSerializer

# Create your views here.


class SpecificationListAPIView(generics.ListAPIView):
    queryset = Specification.objects.filter(is_display=True)
    serializer_class = SpecificationSerializer


class SpecificationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Specification.objects.filter(is_display=True).select_related()
    serializer_class = SpecificationDetailSerializer
    lookup_field = 'slug'
