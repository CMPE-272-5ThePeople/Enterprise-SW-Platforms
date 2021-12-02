from rest_framework.routers import SimpleRouter
from .views import DocumentViewset
router = SimpleRouter()
router.register('documents', DocumentViewset)
urlpatterns = router.urls
