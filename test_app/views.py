from rest_framework import viewsets

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