#!/bin/bash

cd ..

# Собираем image с тегом my_tests
docker build -t my_test2 .

# Запускаем контейнер под именем my_run из image my_tests
docker run --name my_test7777 my_test2 --browser chrome

# Копируем из контейнера созданный allure-result
docker cp my_test7777:/app/allure-result .


# Запускаем хост для отчёта аллюр (утилита лежит локально)
# Хост отчёта нужно будет остановить руками
# Сылка на алюр должна быть своя
/Volumes/WDCWD/Downloads/selenium/allure/bin/allure serve allure-result/

# Удаляем из системы созданный контейнер
#docker system prune -f