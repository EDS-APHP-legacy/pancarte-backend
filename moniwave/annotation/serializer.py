from rest_framework import serializers

from annotation.mapped_models import AnnotationType, AnnotationTimerange, AnnotationTimestamp


class MappedObjectSerializer(serializers.Serializer):

    def create(self, validated_data):
        return self.cls.insert(**validated_data)

    def update(self, instance, validated_data):
        for field in instance.required_fields:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        return instance


class AnnotationTypeSerializer(MappedObjectSerializer):
    cls = AnnotationType

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


class AnnotationTimestampSerializer(MappedObjectSerializer):
    cls = AnnotationTimestamp

    id = serializers.IntegerField(read_only=True)
    source_id = serializers.IntegerField()
    type_id = serializers.IntegerField()
    value = serializers.FloatField()
    comment = serializers.CharField()
    timestamp_micros = serializers.IntegerField()


class AnnotationTimerangeSerializer(MappedObjectSerializer):
    cls = AnnotationTimerange

    id = serializers.IntegerField(read_only=True)
    source_id = serializers.IntegerField()
    type_id = serializers.IntegerField()
    value = serializers.FloatField()
    comment = serializers.CharField()
    start_micros = serializers.IntegerField()
    end_micros = serializers.IntegerField()
