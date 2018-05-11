from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import server_error, bad_request
from rest_framework.response import Response

from annotation.mapped_models import AnnotationType, AnnotationTimerange, AnnotationTimestamp
from annotation.serializer import AnnotationTypeSerializer, AnnotationTimerangeSerializer, AnnotationTimestampSerializer
from utils.exceptions import already_exists, does_not_exists


@permission_classes((permissions.AllowAny,))  # TODO: fix
class MappedObjectViewSet(viewsets.ViewSet):
    mapped_object_class = None
    serializer_class = None

    def list(self, request):
        serializer = self.serializer_class(instance=self.mapped_object_class.get(), many=True)
        return Response(serializer.data)

    def create(self, request):
        fields = {}
        try:
            for field in self.mapped_object_class.required_fields:
                fields[field] = request.POST[field]
            new_ann_type = self.mapped_object_class.insert(**fields)
        except KeyError:
            return bad_request(request, None)
        except RuntimeError:
            return already_exists()
        serializer = self.serializer_class(instance=new_ann_type)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            ann = self.mapped_object_class.get(id=pk)[0]
        except IndexError:
            return does_not_exists()
        serializer = self.serializer_class(instance=ann)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            ann = self.mapped_object_class.get(id=pk)[0]
        except IndexError:
            return does_not_exists()
        try:
            for field in self.mapped_object_class.required_fields:
                setattr(ann, field, request.POST.get(field, getattr(ann, field)))
            ann.update()
        except KeyError:
            return bad_request(request, None)
        except RuntimeError:
            return server_error(request, None)
        serializer = self.serializer_class(instance=ann)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        try:
            ann = self.mapped_object_class.get(id=pk)[0]
            ann.delete()
        except IndexError:
            return does_not_exists()
        except RuntimeError:
            return server_error(request, None)
        return Response({})


class AnnotationTypeViewSet(MappedObjectViewSet):
    mapped_object_class = AnnotationType
    serializer_class = AnnotationTypeSerializer


class AnnotationTimestampViewSet(MappedObjectViewSet):
    mapped_object_class = AnnotationTimestamp
    serializer_class = AnnotationTimestampSerializer


class AnnotationTimerangeViewSet(MappedObjectViewSet):
    mapped_object_class = AnnotationTimerange
    serializer_class = AnnotationTimerangeSerializer
