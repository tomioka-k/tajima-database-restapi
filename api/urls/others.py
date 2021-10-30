from django.urls import path
from api.views.specification_category import BaseListAPIView, MethodCategoryListAPIView, MethodListAPIView, MethodRetrieveAPIView, PasteListAPIView, WalkListAPIView


urlpatterns = [
    # others
    path('method-category/', MethodCategoryListAPIView.as_view(),
         name="method-category"),
    path('method/', MethodListAPIView.as_view(), name="method"),
    path('method/<str:slug>/', MethodRetrieveAPIView.as_view(), name="method-detail"),
    path('base/', BaseListAPIView.as_view(), name="base"),
    path('paste', PasteListAPIView.as_view(), name="paste"),
    path('walk/', WalkListAPIView.as_view(), name="walk"),
]
