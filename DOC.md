Запуск проекта:
    docker-compose up -d --build

    Миграции по БД:
        docker-compose exec web sh
        
        python manage.py migrate

Базовый URL:
    http://127.0.0.1:8000/api/

Относительный URL:    
        interview/ для создания опроса
            POST

            title название
            date_start  старта
            date_end дата окончания
            text_interview описание
\
        choice/ для создания типа вопроса
            POST

            title тип вопроса
\
        question/ для создания вопроса
            POST
                        
            interview название опроса
            text_question текст вопроса
            type_question тип вопроса
            text_answer ответ текстом
\
        choice_answer/ для создания варианта ответа
            POST

            quest текст вопроса
            answer выбор варианта
            answers выбор вариантов
