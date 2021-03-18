from django.conf.urls import url
from django.urls import include
from rest_framework_nested import routers

from .views import LocationViewSet

router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet, basename="location")

urlpatterns = [
    url(r'^', include(router.urls)),
]
