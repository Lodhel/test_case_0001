from django.db import models
from django.contrib.postgres.fields import ArrayField


class Interview(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name='название')
    date_start = models.DateField(verbose_name='дата старта')
    date_end = models.DateField(verbose_name='дата окончания')
    text_interview = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title


class Choice(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name='тип вопроса')

    def __str__(self):
        return self.title


class Question(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, verbose_name='название опроса')
    text_question = models.TextField(verbose_name='текст вопроса')
    type_question = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name='тип вопроса', null=True)
    text_answer = models.TextField(null=True, verbose_name='ответ текстом')

    def __str__(self):
        return self.text_question


class ChoiceAnswer(models.Model):
    quest = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='текст вопроса')
    answer = models.CharField(max_length=1024, null=True, verbose_name='выбор варианта')
    answers = ArrayField(models.CharField(max_length=1024), null=True, verbose_name='выбор вариантов')

    def __str__(self):
        return self.quest
