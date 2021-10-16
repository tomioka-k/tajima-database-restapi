from django.urls import path
from .views import SpecificationListAPIView, SpecificationRetrieveAPIView, SpecificationDocumentListAPIView, SpecificationComposeListAPIView

urlpatterns = [
    path('specification/', SpecificationListAPIView.as_view(),
         name="specification-list"),
    path('specification/<str:slug>/', SpecificationRetrieveAPIView.as_view(),
         name="specification-detail"),
    path('specification/<str:slug>/document/',
         SpecificationDocumentListAPIView.as_view(), name="specification-document"),
    path('specification/<str:slug>/sub_process/', SpecificationComposeListAPIView.as_view(),
         name='specification-sub-process'),
]
