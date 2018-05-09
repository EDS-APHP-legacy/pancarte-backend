from hospital.views import HospitalViewSet, ServiceViewSet, UnitViewSet, BedViewSet
from utils.custom_rest import HybridRouter

router = HybridRouter()
router.register(r'hospital', HospitalViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'unit', UnitViewSet)
router.register(r'bed', BedViewSet)
