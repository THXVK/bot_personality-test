FROM python:3.13-slim

# Создаем непривилегированного пользователя
RUN useradd -m appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

WORKDIR /app

# Устанавливаем системные зависимости (если нужны)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости отдельно для кэширования
COPY --chown=appuser:appuser requirements.txt .

# Создаем venv и устанавливаем зависимости
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt && \
    chown -R appuser:appuser /opt/venv

# Копируем основной код
COPY --chown=appuser:appuser . .

# Настраиваем окружение
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Переключаемся на непривилегированного пользователя
USER appuser

# Запускаем приложение
CMD ["python", "code/main.py"]