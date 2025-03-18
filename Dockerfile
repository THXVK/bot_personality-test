FROM python:3.13-slim

# Установка рабочей директории
WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Указываем виртуальное окружение по умолчанию
ENV PATH="/opt/venv/bin:$PATH"

# Команда для запуска бота
CMD ["python", "code/main.py"]