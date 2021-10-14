from django.db.models import fields
from rest_framework import serializers
from database.models.specification import Method, Specification
from database.models.document import SpecificationDocument


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

    class Meta:
        model = Specification
        exclude = ('is_display', 'creater', 'created_at', 'updated_at')
