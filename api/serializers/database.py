from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from database.models.specification import Base, Method, MethodCategory, Paste, Specification, SpecificationProcess, SpecificationCompose, Walk
from database.models.document import SpecificationDocument, MaterialDocument
from database.models.material import Material


class MaterialDocumentSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = MaterialDocument
        fields = ('category', 'file')


class MaterialSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    document = MaterialDocumentSerializer(many=True)

    class Meta:
        model = Material
        fields = ('slug', 'name', 'category', 'normalize_name',
                  'standard', 'material_image', 'document')


class SpecificationProcessSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    unit = serializers.CharField(source='get_unit_display')

    class Meta:
        model = SpecificationProcess
        fields = (
            "order",
            "material",
            "min_quantity",
            "max_quantity",
            "unit",
            "remarks",
        )


class SpecificationDocumentSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = SpecificationDocument
        fields = ('category', 'file')


class MethodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MethodCategory
        fields = ('id', 'name')


class MethodSeriarizer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Method
        fields = ('id', 'category', 'name', 'normalize_name')


class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Base
        fields = ('id', 'name')


class PasteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paste
        fields = ('id', 'name')


class WalkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Walk
        fields = ('id', 'name')


class SpecificationSerializer(serializers.ModelSerializer):

    method = MethodSeriarizer(read_only=True)
    base = serializers.StringRelatedField(many=True)
    part = serializers.StringRelatedField()
    paste = serializers.StringRelatedField()
    walk = serializers.StringRelatedField()

    class Meta:
        model = Specification
        fields = ('slug', 'name', 'method', 'method_name', 'description', 'base',
                  'part', 'paste', 'walk', 'is_insulation', 'remarks', 'image')


class SpecificationDetailSerializer(serializers.ModelSerializer):

    method = MethodSeriarizer(read_only=True)
    base = serializers.StringRelatedField(many=True)
    part = serializers.StringRelatedField()
    paste = serializers.StringRelatedField()
    walk = serializers.StringRelatedField()
    slope = serializers.StringRelatedField()
    process = SpecificationProcessSerializer(
        many=True, read_only=True)

    class Meta:
        model = Specification
        fields = ('slug', 'name', 'method_name', 'method', 'description', 'part', 'paste', 'walk', 'base', 'slope', 'is_insulation',
                  'weight', 'thickness', 'co2_usage', 'service_life', 'remarks', 'image', 'interface', 'cad', 'process')


class SpecificationProcessSerializer(serializers.ModelSerializer):

    method = MethodSeriarizer(read_only=True)
    process = SpecificationProcessSerializer(
        many=True, read_only=True)

    class Meta:
        model = Specification
        fields = ('slug', 'name', 'method_name',
                  'method', 'remarks', 'process')


class SpecificationComposeSerializer(serializers.ModelSerializer):

    name = StringRelatedField(source='sub_specification')
    specification = SpecificationDetailSerializer(source='sub_specification')

    class Meta:
        model = SpecificationCompose
        fields = ('order', 'name', 'specification',
                  )
