# Используйте базовый образ Python
FROM python:3.10

# Создайте рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте все файлы вашего приложения в контейнер
COPY . /app

# Установите зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Запустите ваше приложение (примерно так, но может зависеть от вашего проекта)
CMD ["python", "main.py"]
