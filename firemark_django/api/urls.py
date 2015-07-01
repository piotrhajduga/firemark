from django.conf.urls import include, url
from rest_framework import routers
from locations.views import (
    LocationViewSet,
    LocationExitViewSet,
    LocationItemViewSet,
)

router = routers.DefaultRouter()
router.register(r'location', LocationViewSet, base_name="location")
router.register(r'location_exit', LocationExitViewSet,
                base_name="location_exit")
router.register(r'location_item', LocationItemViewSet,
                base_name="location_item")

urlpatterns = router.urls + [
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]
