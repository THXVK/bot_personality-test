import asyncio
import logging

from aiogram import Bot, Dispatcher
#  from log import logger
from bot import router
from logger import logger
from config import TOKEN
from data import create_table

bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    await create_table()
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('работа приостановлена')
