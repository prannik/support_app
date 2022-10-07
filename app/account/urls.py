from rest_framework.routers import DefaultRouter

from app.account.views import AuthViewSet

router = DefaultRouter()
router.register('', AuthViewSet, 'auth')

urlpatterns = router.urls
