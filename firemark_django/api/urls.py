from django.conf.urls import include, url
from rest_framework import routers
from locations.views import LocationViewSet

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet, base_name="locations")

urlpatterns = router.urls + [
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]
