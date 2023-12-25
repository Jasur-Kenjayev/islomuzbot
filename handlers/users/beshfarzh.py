from aiogram.types import Message
from loader import dp

@dp.message_handler(text="📿 Iymon")
async def iymonf(message:
Message):
	await message.answer("<b>📿 Iymon haqida!\n\n📇 https://telegra.ph/Iymon-haqida-02-26\n\n✅ @islom_namoz_bot</b>")
	
@dp.message_handler(text="🧎Namoz")
async def namozf(message:
Message):
	await message.answer("<b>🧎‍♂️Namoz haqida!\n\n📇 https://telegra.ph/Namoz-haqida-02-26\n\n✅ @islom_namoz_bot</b>")
	
@dp.message_handler(text="🤝 Zakot")
async def Zakotf(message:
Message):
	await message.answer("<b>🤝 Zakot Haqida!\n\n📇 https://telegra.ph/Zakot-haqida-02-26\n\n✅ @islom_namoz_bot</b>")
	
@dp.message_handler(text="🤐 Ro'za")
async def Rozaf(message:
Message):
	await message.answer("<b>🤐 Ro'za Haqida!\n\n📇 https://telegra.ph/Roza-haqida-02-26\n\n✅ @islom_namoz_bot</b>")
	
@dp.message_handler(text="🕋 Haj")
async def hajfuncsi(message:
Message):
	await message.answer("<b>🕋 Haj Haqida!\n\n📇 https://telegra.ph/Haj-haqida-02-26\n\n✅ @islom_namoz_bot</b>")