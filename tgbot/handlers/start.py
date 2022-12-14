from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart

async def bot_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons =["7","8","9"]
    keyboard.add(*buttons)
    await message.answer(text="выбери свой класс", reply_markup=keyboard)
    


def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
