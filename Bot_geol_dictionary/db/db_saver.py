import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import FSInputFile
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

logger = logging.getLogger(__name__)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
async def main():
    BOT_TOKEN = '6054779759:AAE8JqMOb0O6BHmngBGjOyjXZoiKPAFVUNQ'

    bot: Bot = Bot(BOT_TOKEN)
    dp: Dispatcher = Dispatcher()

    #file = open('db_users.json','rb')
    file_up = FSInputFile('db_users.json')
    #file = open('db_users.json','rb')
    await bot.send_document(658548776, file_up)

if __name__ == '__main__':
    try:
        # Запускаем функцию main
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')