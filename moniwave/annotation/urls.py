from utils.custom_rest import HybridRouter

router = HybridRouter()
router.register(r'types', HospitalViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'unit', UnitViewSet)
router.register(r'bed', BedViewSet)