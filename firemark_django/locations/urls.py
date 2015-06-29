from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'locations', views.LocationViewSet)

urlpatterns = router.urls
