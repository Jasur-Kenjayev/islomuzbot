from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, bot

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
	text = "<b>🤖 Ushbu bot barcha Musulmonlar uchun dasturlab chiqildi.\n\n🤖 Bot hozirda 1.0 Versiyada ishlamoqda\n\n✅ @islom_namoz_bot</b>"
	await message.answer(text)