# Используем базовый образ Python 3.13
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код (папку code и файл .env)
COPY code ./code
COPY .env .

# Команда для запуска бота
CMD ["python", "code/main.py"]