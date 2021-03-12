from django.conf.urls import url
from django.urls import include
from rest_framework_nested import routers

from .views import (
    LocationViewSet,
    LocationExitViewSet,
    LocationItemViewSet,
)

router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet, basename="location")

locations_router = routers.NestedSimpleRouter(router, r'locations', lookup='location')
locations_router.register(r'exits', LocationExitViewSet, basename="location_exit")
locations_router.register(r'items', LocationItemViewSet, basename="location_item")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(locations_router.urls)),
]
