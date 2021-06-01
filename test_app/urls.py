from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('profile', views.InterviewViewSet)
router.register('login', views.ChoiceViewSet)
router.register('category', views.QuestionViewSet)
router.register('tag', views.ChoiceAnswerViewSet)