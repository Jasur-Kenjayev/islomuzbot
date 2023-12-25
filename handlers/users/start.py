import sqlite3
from aiogram.types import ParseMode, Message
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import Menu
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
    	pass

    await message.answer(f"*Assalomu Alaykum va Rahmatullohu va Barokatuh\n\n😊 Aziz Dindoshim {message.from_user.full_name}\n📿Alloh Taalo Sizu Bizni Musulmon Qilib Yaratganiga Shu Kunlarga Yetkazganiga Shukurlar Bo'lsin!\n\n✨ Maqsadimiz — Muhammad(s.a.v) Ummatiga Oz Bo'lsada Manfaat Yetkazish.*",parse_mode=ParseMode.MARKDOWN,reply_markup=Menu)
    count = db.count_users()[0]
    msg = f"*{message.from_user.full_name} 💡Bazaga Yangi 👤Foydalanuvchi ➕Qo'shildi. Bazada {count} ta Foydalanuvchi Bor✅*"
    await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode=ParseMode.MARKDOWN)