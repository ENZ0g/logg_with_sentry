Цель проекта - проверить сервис [sentry.io](https://sentry.io)

Для этого был создан простой bottle сервер с двумя путями:
- `/success`  возвращающий статус-код 200
- `/fail`     вызывающий RuntimeError, соответсвенно вызывающий статус-код 500

Сразу после регистрации, sentry предлагает выбрать платформу проекта. Выбираем bottle и сервис тут же дает готовые куски кода с настройками. Вствляем их в код нашего сервера и интеграция готова!
****
Далее я оставлю шпаргалку по командам cmd, чтобы они, наконец, были у меня в одном месте:
### Создание виртуального окружения:

- Вызываем консоль и прописываем:

	`python -m venv project_name`

- Активируем окружение:

	`project_name\Scripts\activate`

### Деплой на Heroku:

- Нам понадобятся следющие дополнительные файлы:

	`requirements.txt` 	- список дополнительных библиотек, можно получить командой `pip freeze > requirements.txt`
	`runtime.txt`		- версия Python для запуска приложения (в моем случае python-3.7.0)
	`Procfile`		- команда, которую выполнит Heroku при запуске моего приложения(в данном случае там будет:: 				`web: python server.py`)

- Для начала нужно запустить контроль версий:

	`git init`

- Если есть файлы и папки, за которым не нужно следить:
	
	создать файл .gitignore (`gitignire.txt ->> cmd$ ren gitignore.txt .gitignore`)
	например, в данном случае у него такое содержание:
					TIPS virtenv and deploy.txt
					/tests.py
					/logger_venv/*
					.*

- Добавляем и коммитим отслеживаемые файлы:

	`git add -A`
	`git commit -m "first commit"`

- Создаем репозиторий на GitHub. После этого связываем его с локальным:

	`git remote add origin https://github.com/ENZ0g/logg_with_sentry`

- Отправляем изменения на GitHub:

	`git push -u origin master`

	ПОСЛЕДНИЕ ДВА ПУНКТА НЕОБХОДИМЫ, ЕСЛИ НУЖНО ЗАЛИТЬ РЕПОЗИТОРИЙ НА GITHUB. ДЛЯ ДЕПЛОЯ НА HEROKU ЭТО МОЖНО НЕ ДЕЛАТЬ.

- Собственно, деплой:

    `heroku create`

- Определяем переменные окружения:

    `heroku config:set APP_LOCATION=heroku`
    `heroku config:set DSN={your_sentry_dsn}`

- Загружаем код на heroku:

    `git push heroku master`

- Запускаем сервер:

    `heroku ps:scale web=1`
