from django.urls import path
from api.views.specification import SpecificationListAPIView, SpecificationRetrieveAPIView, SpecificationDocumentListAPIView, SpecificationComposeListAPIView
from api.views.specification_category import BaseListAPIView, MethodCategoryListAPIView, MethodListAPIView, PasteListAPIView, WalkListAPIView


urlpatterns = [
    # specification
    path('', SpecificationListAPIView.as_view(), name="specification-list"),
    path('<str:slug>/', SpecificationRetrieveAPIView.as_view(),
         name="specification-detail"),
    path('<str:slug>/document/',
         SpecificationDocumentListAPIView.as_view(), name="specification-document"),
    path('<str:slug>/sub_process/', SpecificationComposeListAPIView.as_view(),
         name='specification-sub-process'),
]
