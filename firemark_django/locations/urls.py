from rest_framework import routers
from .views import (
    LocationViewSet,
    LocationExitViewSet,
    LocationItemViewSet,
)

router = routers.SimpleRouter()
router.register(r'location', LocationViewSet, base_name="location")
router.register(r'location_exit', LocationExitViewSet,
                base_name="location_exit")
router.register(r'location_item', LocationItemViewSet,
                base_name="location_item")

urlpatterns = router.urls
