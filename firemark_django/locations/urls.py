from django.urls import include, path
from rest_framework_nested import routers

from .views import LocationViewSet

router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet, basename="location")

urlpatterns = [
    path('', include(router.urls)),
]
