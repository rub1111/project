import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from routers import secretary


TOKEN = "TOKEN"

dp = Dispatcher()
dp.include_router(secretary)
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    kb = [
        [
            KeyboardButton(text="Товары 🛒"),
            KeyboardButton(text="Профиль 👤")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Приветствую в нашем магазине!"
    )
    await message.answer(f"Привет!, {message.from_user.full_name}!", reply_markup=keyboard)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())