from rest_framework import routers, urlpatterns
from .api import ApiViewset

router = routers.DefaultRouter()
router.register('api/jia', ApiViewset, 'apis')

urlpatterns = router.urls