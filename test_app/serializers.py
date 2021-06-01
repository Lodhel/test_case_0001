from django.db import transaction
from rest_framework import serializers
from . import models


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Interview
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.save()
        return instance


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.save()
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.save()
        return instance


class ChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChoiceAnswer
        fields = '__all__'

    @transaction.atomic()
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = '__all__'
