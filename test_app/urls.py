from rest_framework.routers import DefaultRouter

from django.conf.urls import url, include
from . import views


router = DefaultRouter()
router.register('interview', views.InterviewViewSet)
router.register('choice', views.ChoiceViewSet)
router.register('question', views.QuestionViewSet)
router.register('choice_answer', views.ChoiceAnswerViewSet)
router.register('answer', views.AnswerViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^login/?$', views.LoginAPIView.as_view())
]