#!/bin/bash

FILE=env/

apt update
apt install python3

if [ ! -d "$FILE" ]; then
    python3 -m venv env
fi

source env/bin/activate && pip install -U pip && pip install -r requirements.txt

docker build -t my_test1 .

# Запускаем контейнер под именем my_run из image my_tests
#docker run --name my_run my_test --browser chrome

# Копируем из контейнера созданный allure-report
#docker cp my_run:/app/allure-report .
