# Yatube
Сайт для публикации личных дневников.

### Инструкция для развертывания проекта локально
- Клонируйте репозиторий:  
```git clone https://github.com/Andrey-666/hw05_final.git```
- Перейдите в директорию с проектом
- Создайте файл *.env*, в котором укажите переменную окружения *SECRET_KEY*.
- Создайте виртуальное окружение:  
```python -m venv venv```
- Активируйте виртуальное окружение:  
для windows: ```source venv/Scripts/activate```  
для linux: ```source venv/bin/activate```
- Установите зависимости:  
```pip install -r requirements.txt```
- Выполните миграции:  
```python manage.py migrate```
- запустите сервер Django:  
```python manage.py runserver```

***
### Об авторе  
Кузнецов Андрей    
<andrey.66677@yandex.ru>

### Используемые технологии 
- [Python 3.8.5](https://www.python.org/)
- [Django 2.2.16](https://www.djangoproject.com/)
