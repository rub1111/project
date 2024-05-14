from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

secretary = Router()


def services_kb():
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(
        text="Услуга 1", callback_data="payment")
    )
    builder.row(InlineKeyboardButton(
        text="Услуга 2", callback_data="payment")
    )
    builder.row(InlineKeyboardButton(
        text="Услуга 3", callback_data="payment")
    )
    return builder


def put_money_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="Пополнить баланс 💲", callback_data="payment")
    )
    return builder


@secretary.message()
async def add_task(message: Message):
    
    balance = 0
    if message.text == "Профиль 👤":
        builder = put_money_kb()
        await message.answer(f"Ваш профиль 👤\nБаланс {balance} руб", reply_markup=builder.as_markup()) 

    elif message.text == "Товары 🛒":
        builder = services_kb()
        await message.answer(f"Вот список наших услуг 🛍️", reply_markup=builder.as_markup())
        

@secretary.callback_query()
async def payment_failed(call: CallbackQuery):
    await call.message.answer("Платежная система в даненый момент не доступна (")