from rest_framework import serializers

from hospital.models import Hospital, Service, Unit, Bed


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateField(read_only=True)


class HospitalSerializer(BaseSerializer):
    name = serializers.CharField(max_length=254)
    alias = serializers.CharField(read_only=True)

    class Meta:
        model = Hospital
        fields = ('id', 'created_at', 'name', 'alias')


class ServiceSerializer(BaseSerializer):
    name = serializers.CharField(max_length=254)
    alias = serializers.CharField(read_only=True)
    hospital = serializers.PrimaryKeyRelatedField(queryset=Hospital.objects)

    class Meta:
        model = Service
        fields = ('id', 'created_at', 'name', 'alias', 'hospital')


class UnitSerializer(BaseSerializer):
    name = serializers.CharField(max_length=254)
    alias = serializers.CharField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects)

    class Meta:
        model = Unit
        fields = ('id', 'created_at', 'name', 'alias', 'service')


class BedSerializer(BaseSerializer):
    name = serializers.CharField(max_length=254)
    alias = serializers.CharField(read_only=True)
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects)

    class Meta:
        model = Bed
        fields = ('id', 'created_at', 'name', 'alias', 'unit')
