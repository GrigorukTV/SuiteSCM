Проект: SuiteCRM

Проект на Docker hub: https://hub.docker.com/r/bitnami/suitecrm/

Git: https://github.com/GrigorukTV/SuiteSCM

Запуск приложения, БД, phpMyAdmin с помощью docker-compose: в папке  suitecrm docker-compose 
выполнить  - docker-compose up -d

Запуск Jenkins в docker: перейти в папку jenkins и выполнить - docker-compose up -d

Удаленный запуск тестов в Jenkins pipeline: в jenkins pipeline указать 
ссылку  git на файл Jenkinsfile. Добавить параметры для запуска тестов.

Параметры запуска автотестов: 
--browser - выбор браузера, по умолчанию chrome
--url - выбор url для запуска тестов, по умолчанию http://192.168.0.13
--bversion - выбор версии браузера, по умолчанию 87.0
-n - параллельный запуск тестов
--vnc - запись видео в Selenoid UI, по умолчанию True
--logs - запись логов в Selenoid UI, по умолчанию True
--video - запись видео в Selenoid UI, по умолчанию True
--executor - url на Selenoid Hub, по умолчанию 192.168.0.13
