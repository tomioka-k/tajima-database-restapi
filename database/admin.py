from django.contrib import admin
from .models.specification import MethodCategory, Method, Base, Slope, Part, Paste, Walk, Specification, SpecificationProcess
from .models.document import SpecificationDocumentCategory, SpecificationDocument
from .models.material import MaterialCategory, Material


admin.site.register(MethodCategory)
admin.site.register(Method)
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


admin.site.register(SpecificationProcess)
admin.site.register(SpecificationDocumentCategory)
admin.site.register(SpecificationDocument)

admin.site.register(MaterialCategory)
admin.site.register(Material)
