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

    def make_struct(self, data):
        return {
            'answer': data.answer
        }

    def list(self, request, *args, **kwargs):
        question = request.query_params.get('quest', None)
        instance = models.Answer.objects.filter(quest=question)
        if question:
            data = [self.make_struct(case) for case in instance]
            return JsonResponse({'data': data})
        else:
            return super().list(request)


class LoginAPIView(View):
    def post(self, request):
        email = request.POST.get('email', None)
        if not email:
            return JsonResponse({"error": "KeyError"})
        user = User.objects.filter(email=email).first()
        if not user:
            return JsonResponse({"id": None, "username": None})
        return JsonResponse({"id": user.pk, "username": user.username})


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AnswerSerializer
    queryset = models.Answer.objects.all()

    def answer_text(self, user, answer, question):
        data = {
            'user': user,
            'answer': answer,
            'question': question
        }
        instance = models.Answer(**data)
        instance.save()
        return data

    def answer_field(self, user, answer, question):
        data = {
            'user': user,
            'answer': answer,
            'question': question
        }
        instance = models.Answer(**data)
        instance.save()
        return data

    def answer_fields(self, user, answer, questions):
        data = {
            'user': user,
            'answer': answer,
            'question': questions
        }
        instance = models.Answer(**data)
        instance.save()
        return data

    def create(self, request, *args, **kwargs):
        question = request.data.get('question', None)
        user = request.data.get('user', None)
        answer = request.data.get('answer', None)
        answers = request.data.get('answers', None)

        if not question:
            JsonResponse({"error": "KeyError"})

        question_instance = models.Question.objects.filter(id=question).first()
        if not question_instance:
            JsonResponse({"error": "KeyError"})

        type_question = question_instance.type_question.title
        if type_question == 'ответ текстом':
            return JsonResponse(self.answer_text(user, answer, question))

        if type_question == 'ответ с выбором одного варианта':
            return JsonResponse(self.answer_field(user, answer, question))

        if type_question == 'ответ с выбором нескольких вариантов':
            return JsonResponse(self.answer_fields(user, answers, question))
