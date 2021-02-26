Проект: SuiteCRM

Проект на Docker hub: https://hub.docker.com/r/bitnami/suitecrm/
Запуск приложения, БД, phpmyadmin с помощью docker-compose: 
Запуск Jenkins в docker:
Удаленный запуск тестов в Dockerfile:

Параметры запуска автотестов: 
--browser - выбор браузера, по умолчанию chrome
--url - выбор url для запуска тестов, по умолчанию http://192.168.0.13
--bversion - выбор версии браузера, по умолчанию 87.0
- n - параллельный запуск тестов
--vnc - запись видео в Selenoid UI, по умолчанию True
--logs - запись логов в Selenoid UI, по умолчанию True
--video - запись видео в Selenoid UI, по умолчанию True
--executor - url на Selenoid Hub, по умолчанию 192.168.0.13
