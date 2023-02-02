from aiogram import types, executor
from aiogram.dispatcher.filters import Text
import logging
from conf import dp
import asyncio
from modules_pro.start import start_command
from modules_pro.help import help_command
from modules_pro.remin_bot import remind_commands, schedule_command, schedule


async def startup(_):
    """
        Асинкхронная функция для старта сторонних сервисов
    """
    asyncio.create_task(schedule())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(help_command, text='help')
    dp.register_callback_query_handler(remind_commands, text='remind')
    dp.register_message_handler(schedule_command, Text(startswith='напомни'))

    executor.start_polling(dp, skip_updates=True, on_startup=startup)