# Generated by Django 3.2.3 on 2021-06-01 13:30

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='название')),
                ('date_start', models.DateField(verbose_name='дата старта')),
                ('date_end', models.DateField(verbose_name='дата окончания')),
                ('text_interview', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.TextField(verbose_name='текст вопроса')),
                ('text_answer', models.TextField(null=True, verbose_name='ответ текстом')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.interview', verbose_name='название опроса')),
                ('type_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.choice', verbose_name='тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1024, null=True, verbose_name='выбор варианта')),
                ('answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), null=True, size=None, verbose_name='выбор вариантов')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.question', verbose_name='текст вопроса')),
            ],
        ),
    ]