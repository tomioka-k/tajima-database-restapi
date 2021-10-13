from django.db.models import fields
from rest_framework import serializers
from database.models.specification import Specification
from database.models.document import SpecificationDocument


class SpecificationDocumentSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = SpecificationDocument
        fields = ('category', 'file')


class SpecificationSerializer(serializers.ModelSerializer):

    base = serializers.StringRelatedField(many=True)
    part = serializers.StringRelatedField()
    paste = serializers.StringRelatedField()
    walk = serializers.StringRelatedField()

    class Meta:
        model = Specification
        fields = ('id', 'name', 'method_name', 'description', 'base',
                  'part', 'paste', 'walk', 'is_insulation', 'remarks', 'image')


class SpecificationDetailSerializer(serializers.ModelSerializer):

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
