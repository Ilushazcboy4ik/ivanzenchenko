from aiogram import Dispatcher, types
from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart

async def bot_classes_9(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons =["тут типа страницы"]
    keyboard.add(*buttons)
    await message.answer(text="9", reply_markup=keyboard)
    


def register_classes_9(dp: Dispatcher):
    dp.register_message_handler(bot_classes_9, text="9")