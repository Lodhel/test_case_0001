Запуск проекта:
    docker-compose up -d --build

    Миграции по БД:
        docker-compose exec web sh
        
        python manage.py migrate

Базовый URL:
    http://127.0.0.1:8000/api/

Относительный URL:    
        interview/
        choice/
        question/
        choice_answer/