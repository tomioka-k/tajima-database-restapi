from django.contrib import admin
from .models.specification import Category, Base, Specification
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'description')


admin.site.register(Base)
admin.site.register(Specification)
