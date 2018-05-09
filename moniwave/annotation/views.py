from rest_framework import viewsets
from rest_framework.response import Response

from annotation.mapped_models import AnnotationType
from annotation.serializer import AnnotationTypeSerializer


class AnnotationTypeViewSet(viewsets.ViewSet):
    serializer_class = AnnotationTypeSerializer

    def list(self, request):
        serializer = AnnotationTypeSerializer(instance=AnnotationType.get(), many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
