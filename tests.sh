#!/bin/bash

# Собираем image с тегом my_tests
#docker build -t my_test .

# Запускаем контейнер под именем my_run из image my_tests
docker run my_test --browser chrome

# Копируем из контейнера созданный allure-result
docker cp my_run:/app/allure-results .

# Запускаем хост для отчёта аллюр (утилита лежит локально)
# Хост отчёта нужно будет остановить руками
# Сылка на алюр должна быть своя
#/Volumes/WDCWD/Downloads/selenium/allure/bin/allure serve allure-result/

# Удаляем из системы созданный контейнер
#docker system prune -f