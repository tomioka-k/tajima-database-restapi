from django.contrib import admin
from django.urls import path, include

admin.site.site_title = 'Database'
admin.site.site_header = 'Database'
admin.site.index_title = 'メニュー'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/database/', include('api.urls.others')),
    path('api/database/specification/', include('api.urls.specification')),
]
