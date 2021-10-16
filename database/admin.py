from django.contrib import admin
from django.utils.html import format_html
from .models.specification import MethodCategory, Method, Base, Slope, Part, Paste, Walk, Specification, SpecificationProcess, SpecificationCompose
from .models.document import SpecificationDocumentCategory, SpecificationDocument, MaterialDocumentCategory, MaterialDocument
from .models.material import MaterialCategory, Material


admin.site.register(Slope)
admin.site.register(Part)
admin.site.register(Paste)
admin.site.register(Walk)


class SpecificationDocumentInline(admin.TabularInline):
    model = SpecificationDocument
    fk_name = "specification"
    autocomplete_fields = ('category',)
    extra = 0


class SpecificationProcessInline(admin.TabularInline):
    model = SpecificationProcess
    fk_name = "specification"
    autocomplete_fields = ('material',)
    ordering = ('order',)
    extra = 0


class SpecificationComposeInline(admin.TabularInline):
    model = SpecificationCompose
    fk_name = 'main_specification'
    autocomplete_fields = ('sub_specification',)
    ordering = ('order', )
    extra = 0


@admin.register(MethodCategory)
class MethodCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    search_fields = ('name', 'normalize_name')
    autocomplete_fields = ('category',)
    list_filter = ('category__name', )
    list_display = ('name', 'normalize_name', 'category')


@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    autocomplete_fields = ('method', 'base')
    list_filter = ('method__name', 'base', 'slope', 'part', 'paste',
                   'walk', 'slope', 'is_insulation', 'is_display')
    list_display = ('name', 'method', 'method_name', "part", 'paste',
                    'walk', 'slope', 'is_insulation', 'format_image')

    inlines = [
        SpecificationProcessInline,
        SpecificationComposeInline,
        SpecificationDocumentInline,
    ]

    def format_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="360" />', obj.image.url)

    format_image.short_description = "Image"
    format_image.empty_value_display = 'No Image'


@admin.register(SpecificationProcess)
class SpecificationProcessAdmin(admin.ModelAdmin):
    search_fields = ('material__name', 'specification__name')
    list_display = ('order', 'material', 'specification', 'unit',
                    'min_quantity', 'max_quantity', 'remarks')
    ordering = ('specification', 'order')


@admin.register(SpecificationDocumentCategory)
class SpecificationDocumentCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(SpecificationDocument)
class SpecificationDocumentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'specification__name')
    autocomplete_fields = ('category', 'specification')
    list_display = ('name', 'category', 'specification', 'file_link')
    list_filter = ('category__name',)

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" download>Download</a>', obj.file.url)
        else:
            return "No attachment"

    file_link.allow_tags = True
    file_link.short_description = 'File Download'


@admin.register(SpecificationCompose)
class SpeficificationComposeAdmin(admin.ModelAdmin):
    search_fields = ('main_specification', 'sub_specification')
    list_display = ('order', 'main_specification', 'sub_specification')
    autocomplete_fields = ('main_specification', 'sub_specification')


class MaterialInline(admin.TabularInline):
    model = Material
    fields = ('name', 'normalize_name', 'standard', 'remarks')
    can_delete = False
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return list(super().get_fields(request, obj))


@admin.register(MaterialCategory)
class MaterialCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    inlines = (MaterialInline,)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'normalize_name', 'category', 'standard',
                    'remarks', 'bto', 'format_material_image')
    list_filter = ('category__name', 'bto')
    autocomplete_fields = ('category',)
    ordering = ('name',)

    def format_material_image(self, obj):
        if obj.material_image:
            return format_html('<img src="{}" width="360" />', obj.material_image.url)

    format_material_image.short_description = "Image"
    format_material_image.empty_value_display = 'No Image'


@admin.register(MaterialDocumentCategory)
class MaterialDocumentCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(MaterialDocument)
class MaterialDocumentAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('category', 'material', 'name',
                    'is_display', 'created_at', 'updated_at')
    list_filter = ('is_display', 'category__name')
    autocomplete_fields = ('category', 'material')
