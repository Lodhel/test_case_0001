from rest_framework import viewsets
from django.views import View
from django.http import JsonResponse

from django.contrib.auth.models import User

from . import serializers
from . import models


class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InterviewSerializer
    queryset = models.Interview.objects.all()


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChoiceSerializer
    queryset = models.Choice.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer
    queryset = models.Question.objects.all()


class ChoiceAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChoiceAnswerSerializer
    queryset = models.ChoiceAnswer.objects.all()


class LoginAPIView(View):
    def post(self, request):
        email = request.POST.get('email', None)
        user = User.objects.filter(email=email).first()
        if not user:
            return JsonResponse({"id": None, "username": None})
        return JsonResponse({"id": user.pk, "username": user.username})
