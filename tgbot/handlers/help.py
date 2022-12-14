from aiogram import Dispatcher
from aiogram.types import Message


async def user_help(message: Message):
    await message.reply("если у тебя какие-то проблемы с ботом, напиши @zhoski_gadem")


def register_help(dp: Dispatcher):
    dp.register_message_handler(user_help, commands=["help"], state="*")
