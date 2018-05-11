from annotation.views import AnnotationTypeViewSet, AnnotationTimestampViewSet, AnnotationTimerangeViewSet
from utils.custom_rest import HybridRouter

router = HybridRouter()
router.register(r'types', AnnotationTypeViewSet, base_name='ann_types')
router.register(r'timestamp', AnnotationTimestampViewSet, base_name='ann_timestamps')
router.register(r'timerange', AnnotationTimerangeViewSet, base_name='ann_timeranges')
