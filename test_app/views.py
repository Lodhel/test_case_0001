from rest_framework import viewsets
from django.views import View
from django.http import JsonResponse

from django.db import transaction

from django.contrib.auth.models import User

from . import serializers
from . import models


class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InterviewSerializer
    queryset = models.Interview.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def update(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def destroy(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChoiceSerializer
    queryset = models.Choice.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def update(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def destroy(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer
    queryset = models.Question.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def update(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def destroy(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })


class ChoiceAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChoiceAnswerSerializer
    queryset = models.ChoiceAnswer.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def update(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def destroy(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def list(self, request, *args, **kwargs):
        question = request.query_params.get('quest', None)
        instance = models.Answer.objects.filter(quest=question)
        if question:
            data = [{'answer': case.answer} for case in instance]
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

    def _answer_text(self, user, answer, question):
        data = {
            'user': user,
            'answer': answer,
            'question': question
        }
        instance = models.Answer(**data)
        instance.save()
        return data

    def _answer_field(self, user, answer, question):
        data = {
            'user': user,
            'answer': answer,
            'question': question
        }
        instance = models.Answer(**data)
        instance.save()
        return data

    def _answer_fields(self, user, answer, questions):
        data = {
            'user': user,
            'answer': answer,
            'question': questions
        }
        instance = models.Answer(**data)
        instance.save()
        return data

    @transaction.atomic()
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
            return JsonResponse(self._answer_text(user, answer, question))

        if type_question == 'ответ с выбором одного варианта':
            return JsonResponse(self._answer_field(user, answer, question))

        if type_question == 'ответ с выбором нескольких вариантов':
            return JsonResponse(self._answer_fields(user, answers, question))

    def retrieve(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def update(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })

    def destroy(self, request, *args, **kwargs):
        return JsonResponse({
            'request': 'request of this type is prohibited'
        })
