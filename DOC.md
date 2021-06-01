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

            title название, string
            date_start  дата старта, string
            date_end дата окончания, string
            text_interview описание, string 
\
        interview/ для получения опросов
            GET

\
        choice/ для создания типа вопроса
            POST

            title тип вопроса, string
\
        choice/ для получения типа вопроса
            GET

\
        question/ для создания вопроса
            POST
                        
            interview id опроса, integer
            text_question текст вопроса, string
            type_question id типа вопроса, string
\
        question/ для получения вопросов
            GET

\
        choice_answer/ для создания варианта ответа
            POST

            quest id вопроса, integer
            answer выбор варианта, string
            answers выбор вариантов, string
\
        choice_answer/ для получения вариантов ответа
            GET
            в параметрах урл запроса
            quest id вопроса, integer
\
        answer/ для создания ответа
            POST

            question id вопроса, integer
            user id пользователя, integer
            answer ответ, string
            answers ответы, string
\
        answer/ для получения ответа
            GET