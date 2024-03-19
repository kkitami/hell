import logging
import asyncio
from config import TELEGRAM_TOKEN
from aiogram import Bot, Dispatcher
import handler
async def main():
    # Установка уровня логирования
    logging.basicConfig(level=logging.INFO)
    # Токен вашего бота
    TOKEN = TELEGRAM_TOKEN
    # Создание объектов бота и диспетчера
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(handler.router)
    await dp.start_polling(bot)
# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())