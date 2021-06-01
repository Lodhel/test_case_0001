from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('interview', views.InterviewViewSet)
router.register('choice', views.ChoiceViewSet)
router.register('question', views.QuestionViewSet)
router.register('choice_answer', views.ChoiceAnswerViewSet)