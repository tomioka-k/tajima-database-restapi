from django.db.models import fields
from rest_framework import serializers
from database.models.specification import Method, Specification, SpecificationProcess
from database.models.document import SpecificationDocument
from database.models.material import Material


class SpecificationProcessSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField()
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


class MethodSeriarizer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Method
        fields = ('category', 'name', 'normalize_name')


class SpecificationSerializer(serializers.ModelSerializer):

    method = MethodSeriarizer(read_only=True)
    base = serializers.StringRelatedField(many=True)
    part = serializers.StringRelatedField()
    paste = serializers.StringRelatedField()
    walk = serializers.StringRelatedField()

    class Meta:
        model = Specification
        fields = ('id', 'name', 'method', 'method_name', 'description', 'base',
                  'part', 'paste', 'walk', 'is_insulation', 'remarks', 'image')


class SpecificationDetailSerializer(serializers.ModelSerializer):

    method = MethodSeriarizer(read_only=True)
    base = serializers.StringRelatedField(many=True)
    part = serializers.StringRelatedField()
    paste = serializers.StringRelatedField()
    walk = serializers.StringRelatedField()
    slope = serializers.StringRelatedField()
    document = SpecificationDocumentSerializer(
        many=True, read_only=True)
    process = SpecificationProcessSerializer(
        many=True, read_only=True)

    class Meta:
        model = Specification
        fields = ('id', 'name', 'method_name', 'method', 'description', 'part', 'paste', 'walk', 'base', 'slope', 'is_insulation',
                  'weight', 'thickness', 'co2_usage', 'service_life', 'remarks', 'image', 'interface', 'cad', 'process', 'document')
