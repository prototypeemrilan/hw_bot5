from aiogram import types
from modules_pro.cons import START_TEXT
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

""" Обработчик категорий """
start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(
	InlineKeyboardButton('Уроки', callback_data='remind'),
	InlineKeyboardButton('Помощь', callback_data='help')
)


async def start_command(message: types.Message):
	"""
		Функция приветствия пользовователя
	"""
	await message.answer(text=START_TEXT.format(first_name=message.from_user.first_name), reply_markup=start_kb)
	await message.delete()