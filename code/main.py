import asyncio
from aiogram import Bot, Dispatcher
#  from log import logger


from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
