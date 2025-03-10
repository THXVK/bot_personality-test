import asyncio
import logging

from aiogram import Bot, Dispatcher
#  from log import logger
from bot import router
from config import TOKEN


bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('closed')
