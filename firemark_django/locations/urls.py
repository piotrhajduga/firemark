from rest_framework import routers

from .views import (
    LocationViewSet,
    LocationExitViewSet,
    LocationItemViewSet,
)

router = routers.SimpleRouter()
router.register(r'location', LocationViewSet, basename="location")
router.register(r'location_exit', LocationExitViewSet,
                basename="location_exit")
router.register(r'location_item', LocationItemViewSet,
                basename="location_item")

urlpatterns = router.urls
