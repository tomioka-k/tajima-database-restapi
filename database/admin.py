from django.contrib import admin
from .models.specification import Category, Base, Slope, Part, Paste, Walk, Specification


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'description')


admin.site.register(Base)
admin.site.register(Slope)
admin.site.register(Part)
admin.site.register(Paste)
admin.site.register(Walk)


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'method_name', "part", 'paste',
                    'slope', 'walk', 'is_insulation')
