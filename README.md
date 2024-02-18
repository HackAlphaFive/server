# 🅰️ Микросервис Индивидуальных планов развития сотрудников Альфа-Банка
Сервис, в рамках которого для сотрудников можно составить индивидуальные планы развития (ИПР) с набором необходимых задач, просматривать их и валидировать выполнение целей.

## Документация API в Swagger
https://alfahackathon.hopto.org/api/v1/swagger/

Локально: http://127.0.0.1:8000/api/v1/swagger/ 

## Документация API в Redoc  
https://alfahackathon.hopto.org/api/v1/redoc/

Локально: http://127.0.0.1:8000/api/v1/redoc/

## Инструкция по сборке и запуску
### Локальное развертывание
1. Необходимо переименовать файл .env.example и отредактировать переменные.
2. Создать локальное окружение:
    ```
    python -m venv venv
    ```
3. Запустить локальное окружение:
    ```
    . venv/bin/activate
    ```
4. Установить зависимости:
    ```
    pip install -r requirements.txt
    ```
5. Необходимо в файле ipr/ipr/settings.py закомментировать строку:
    ```
    CSRF_TRUSTED_ORIGINS = ['https://alfahackathon.hopto.org']
    ```
6. Выполнить миграции:
    ```
    cd ipr/
    python manage.py migrate
    ```
7. Загрузить тестовые данные (при необходимости):
    ```
    python manage.py create_mock_data
    ```
8. Запустить сервис разработчика:
    ```
    python manage.py runserver
    ```

### Развертывание на сервере
1. Поменять в следующих файлах название домена на небходимое (по умолчанию: alfahackathon.hopto.org):
- init-letsencrypt.sh
- dockerization/nginx/default.conf
- ipr/ipr/settings.py
2. Проверить Debug режим в ipr/ipr/settings.py
3. Запустить файл init-letsencrypt.sh
    ```
    ./init-letsencrypt.sh
    ```
4. Запустить Docker Compose:
    ```
    docker compose up -d
    ```

## Тестирование
Тестирование производится командой:
```
cd api/
python manage.py test
```

Test coverage ~ 70%

## Стэк технологий  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=react-router&logoColor=white)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)

## Сведения о команде разработки
**Менеджер проекта** - отвечает за синхронизацию Команды, выполнение задач в дедлайны Конкурса и организационные вопросы:   
Андрей Нестеров https://t.me/Agarhim  

**Product-менеджер** – делает: анализ ЦА, прописывает цели, задачи проекта, гипотезы, юзерфлоу (как ни странно, неправда ли), юзерстори, портрет пользователя, рисует макет MVP:    
Вероника Кусакина https://t.me/kuvero  

**SA** – отвечает за технические требования:  
Евгения Новак https://t.me/jane_nova  
Александр Добаков https://t.me/dabakov  

**BA** – отвечает за бизнес требования:  
Лариса Фишер https://t.me/FisherLarisa  
Елизавета  http://t.me/L_t71  

**Дизайнер** — креативщик Команды, отвечает за UI/UX, дизайн макетов:  
Серж https://t.me/BugsBunny313  
Марина Титова https://t.me/marinatitova17  

**Frontend-разработчик** – отвечает за визуализацию данных:  
Максим Бучков https://t.me/popavsi  
Павел Захаров https://t.me/pz1776  
Алексей Тютрин https://t.me/tuxoneee  

**Backend-разработчик** – отвечает за обработку данных:  
Павел Ложкин https://t.me/lozhkin_pa  
Александр Струнский https://t.me/alexstrunskiy  
Максим Спицын https://t.me/maxu_s  
Екатерина Новикова https://t.me/moncher_ii
