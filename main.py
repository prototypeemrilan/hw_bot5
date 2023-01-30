from aiogram import types, executor
from aiogram.dispatcher.filters import Text
import logging
from conf import dp
from modules_pro.start import start_command
from modules_pro.help import help_command
from modules_pro.fms import (
    Form,
    cancel_handler,
    form_start,
    name,
    remind,
    time,
    done,
    napominal,
    scheduler
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(form_start, commands=['form'])
    dp.register_message_handler(form_start, commands=['napominalka'])
    dp.register_message_handler(form_start, Text(equals='Нет'), state=Form.done)
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(name, state=Form.name)
    dp.register_message_handler(remind, state=Form.remind)
    dp.register_message_handler(time, state=Form.time)
    dp.register_message_handler(done, Text(equals='Да'), state=Form.done)
    dp.register_message_handler(napominal, Text(equals='start'), state=Form.start_re)
    dp.register_message_handler(scheduler, commands="start")

    executor.start_polling(dp, skip_updates=True)