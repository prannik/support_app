from rest_framework.routers import DefaultRouter

from app.task.views import AnswerViewSet, ProblemViewSet

router = DefaultRouter()
router.register('', ProblemViewSet, 'task')
router.register('answer', AnswerViewSet, 'answer')

urlpatterns = router.urls
