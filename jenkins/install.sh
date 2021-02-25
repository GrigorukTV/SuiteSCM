#!/bin/bash

FILE=env/

if [ ! -d "$FILE" ]; then
    python3 -m venv env
fi

source env/bin/activate && pip install -U pip && pip install -r requirements.txt --upgrade

docker build -t my_test1 .

# Запускаем контейнер под именем my_run из image my_tests
#docker run --name my_run my_test --browser chrome

# Копируем из контейнера созданный allure-result
#docker cp my_run:/app/allure-result .
