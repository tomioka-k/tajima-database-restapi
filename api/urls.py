from django.urls import path
from .views import SpecificationListAPIView, SpecificationRetrieveAPIView

urlpatterns = [
    path('specification/', SpecificationListAPIView.as_view(),
         name="specification-list"),
    path('specification/<str:id>/', SpecificationRetrieveAPIView.as_view(),
         name="specification-detail"),
]