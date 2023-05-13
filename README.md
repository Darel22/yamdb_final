# CI и CD проекта api_yamdb
![example workflow](https://github.com/darel22/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

http://51.250.80.101/redoc/

В проекте присутствует:
- автоматический запуск тестов,
- обновление образов на Docker Hub,
- автоматический деплой на боевой сервер при пуше в главную ветку main,
- отправка уведомлений в Telegram о том, что процесс деплоя успешно завершился.


Проект представляет собой API для проекта Reviews.

# api_yamdb
>API Reviews - это API без лишних деталей. Благодаря этому его легко освоить и доработать. Через приложение уже можно читать информацию о разных произведениях,оставлять отзывы и комментарии к отзывам. Эту основу легко расширить, добавляя новые возможности.

#### Как запустить проект:

+ клонируем репозиторий `git clone`
`https://github.com/sabina-045/api_yamdb.git`
+ переходим в него `cd api_yamdb`
    + разворачиваем виртуальное окружение
    `python3 -m venv env` (Windows: `python -m venv env`)
    + активируем его
    `source env/bin/activate` (Windows: `source env/scripts/activate`)
    + устанавливаем зависимости из файла requirements.txt
    `pip install -r requirements.txt`
+ выполняем миграции
`python3 manage.py migrate` (Windows: `python manage.py migrate`)
+ запускаем проект
`python3 manage.py runserver` (Windows: `python manage.py runserver).
И вперед!

#### Инструкции и примеры

>Основные эндпойнты `/api/v1/`:

/titles/ - список произведений, создается админом.

/titles/{title_id}/ - информация об отдельном произведении.

/titles/{title_id}/reviews/ - список отзывов к отдельному произведению, создание отзыва.

/titles/{title_id}/reviews/comments/{comment_id}/ - информация об отдельном комментарии, изменение комментария автором или модератором.

#### Для доступа к API необходимо получить токен:

Нужно выполнить POST-запрос http://127.0.0.1:8000/api/v1/auth/signup/ передав поля username и email.

На указанный адрес придет письмо с confirmation_code.
Нужно отправить POST-запрос http://127.0.0.1:8000/api/v1/auth/token/ передав поля username и confirmation_code.

Полученный токен передаем в заголовке Authorization: Bearer <токен>


#### Команда создателей:
Яндекс Практикум, Максим Габчак, Андрей Чернышев, Сабина Гаджиева