import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат сообщений
    filename='app.log',  # Имя файла для логирования
    filemode='a',  # Режим записи: 'a' (append) или 'w' (write)
)

# Создание логгера
logger = logging.getLogger(__name__)


handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024, backupCount=10)  # 1 MB per file, keep 5 backups
logging.basicConfig(handlers=[handler], encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s FILE: %(filename)s IN: %(funcName)s MESSAGE: %(message)s')




