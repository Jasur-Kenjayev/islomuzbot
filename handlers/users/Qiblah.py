from aiogram.types import Message
from loader import dp
from keyboards.inline.savolqibla import Qibla, islomdinimizsavol, Savolbot
from keyboards.default.menu import bekor2, Menu, Savolb
from keyboards.default.foydali import Savol
from states.savol import PersonalData2
from aiogram.dispatcher import FSMContext
from aiogram import types
import requests
import json

@dp.message_handler(text= "↩️ Orqaga",state=PersonalData2.adss2)
async def cancel1(message:
	types.Message, state: FSMContext):
	await state.finish()
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=Savolb)

@dp.message_handler(text= "Orqaga ↪️")
async def cancel2(message:
	types.Message):
	await message.answer("<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>",reply_markup=Savol)
	
	
@dp.message_handler(text="🧭 Qibla Kompus")
async def select_Qibla(message: Message):
    qibla_id = "AgACAgIAAxkBAAIP8mIaMPMMCmAuwJtZKjnyd3HpvdQ5AALfvzEb6tXRSJY970crRxY7AQADAgADeQADIwQ"
    await message.answer_photo(qibla_id, caption=f"<b>🧭 Qibla Kompus Bo'lmidasiz.\n\n🕋 Qibla Qaysi Tarafda ekanligini aniqlash uchun 📍Joylashuv Yani (Location) ni Yoqing Va 👇Pastagi 🌐Saytga O'tish Tugmasni Bosing Va Sayt Sizga 🕋Qibla Qaysi Tarafda Ekanligini Aniqlab Beradi!\n\n✅ @islom_namoz_bot</b>",reply_markup=Qibla)
    
@dp.message_handler(text="🗞 Manbalar")
async def select_Manba(message: Message):
	await message.answer("<b>🤖 Botmizdagi Barcha Malumotlar ishonarli Sayt va Kanallardan Olindi.\n\n🗞 Biz Foydalangan Ⓜ️anbalar\n\n🌐 islom.uz\n🌐 islom.ziyouz.com\n🌐 YouTube.com\n🌐 savollar.islom.uz\n\n✅ @islom_namoz_bot</b>")
	
@dp.message_handler(text="📖 Dinimiz bo'yicha Savol")
async def islomsavol(message: Message):
    savolyi = "AgACAgIAAxkBAAInZGIo3WVVx2QFMROPSm_8N6XrxBdRAAIjvjEb9URJSUjqv4slytlcAQADAgADeAADIwQ"
    await message.answer_photo(savolyi,caption="<i>🤖 Ushbu bo'limda siz yo'lagan savolga o'xshash savollar savollar.islom.uz Saytiga yo'langan bo'lsa o'sha sizning savolingizga o'xshash Savol va Savol Javobi Sizga yuboriladi va o'sha sizning savolingizga o'xshash savolni o'qib chiqib Savolingizga Javob olasiz✅\n\n✅ @islom_namoz_bot</i>",reply_markup=Savolb)
	
@dp.message_handler(text="🤖 Bot bo'yicha Savol")
async def botsavol(message: Message):
	await message.answer("<b>🤖 Bot bo'yicha Savollaringiz bo'lsa quydagi Botga Yo'lashingiz Mumkun👇</b>",reply_markup=Savolbot)
	

@dp.message_handler(text="📝 Savol Yuborish")
async def islomsavol(message: Message):
	await message.answer("<b>✏️ Marhammat Savolingizni Kiriting!</b>",reply_markup=bekor2)
	await PersonalData2.adss2.set()

@dp.message_handler(state=PersonalData2.adss2)
async def savolislom(message: types.Message, state: FSMContext):
    text = message.text
    msg11 = await message.answer('<b>◾️ 10%</b>')
    await msg11.delete()
    msg = await message.answer('<b>◾️◾️ 20%</b>')
    await msg.delete()
    msg1 = await message.answer('<b>◾️◾️◾️ 30%</b>')
    await msg1.delete()
    msg2 = await message.answer('<b>◾️◾️◾️◾️ 40%</b>')
    await msg2.delete()
    msg3 = await message.answer("<b>◾️◾️◾️◾️◾️ 50%</b>")
    await msg3.delete()
    msg4 = await message.answer("<b>◾️◾️◾️◾️◾️◾️ 60%</b>")
    await msg4.delete()
    msg5 = await message.answer("<b>◾️◾️◾️◾️◾️◾️◾️ 70%</b>")
    await msg5.delete()
    msg6 = await message.answer('<b>◾️◾️◾️◾️◾️◾️◾️◾️ 80%</b>')
    await msg6.delete()
    msg7 = await message.answer("<b>◾️◾️◾️◾️◾️◾️◾️◾️◾️ 90%</b>")
    await msg7.delete()
    msg8 = await message.answer("<b>◾️◾️◾️◾️◾️◾️◾️◾️◾️ 100%</b>")
    await msg8.delete()
    msg0 = await message.answer("<b>⏳Biroz Kuting Malummotlar Sizga Yuborilmoqda....</b>")
    
    url = f'https://islomuz.herokuapp.com/api/savol?q={text}'
    r = requests.get(url).json()
    try:
    	bir = (r["results"]["1"]["quest_id"])
    	javob = f"https://islomuz.herokuapp.com/api/savol/{bir}"
    	re = requests.get(javob).json()
    	savolnomi = (re["title"])
    	savolvaqti = (re["quest_time"])
    	savoli = (re["question_text"])
    	javobi = (re["answer_text"])
    	await message.reply(f"<b>📒 Савол номи - {savolnomi}\n⏰ Савол берилган вақти - {savolvaqti}\n\n📝 Савол - {savoli}\n\n📕 Савол Жавоби - {javobi}\n\n🌐Manba - Savollar.islom.uz\n🤖Bot - @islom_namoz_bot</b>")
    except:
    	await message.reply(f"<b>{text} - 📜 Savolingiz bo'yicha hechnimma topilmadi☹️ Ushbu Savolingizni Pastagi Saytga yo'lang albatta javob olasiz Savolingizga👇</b>",reply_markup=islomdinimizsavol)
    try:
    	ikki = (r["results"]["2"]["quest_id"])
    	javob2 = f"https://islomuz.herokuapp.com/api/savol/{ikki}"
    	re2 = requests.get(javob2).json()
    	savolnomi2 = (re2["title"])
    	savolvaqti2 = (re2["quest_time"])
    	savoli2 = (re2["question_text"])
    	javobi2 = (re2["answer_text"])
    	await message.reply(f"<b>📗 Савол номи - {savolnomi2}\n⏰ Савол берилган вақти - {savolvaqti2}\n\n📝 Савол - {savoli2}\n\n📕 Савол Жавоби - {javobi2}\n\n🌐Manba - Savollar.islom.uz\n🤖Bot - @islom_namoz_bot</b>")
    except:
    	pass
    try:
    	uch = (r["results"]["3"]["quest_id"])
    	javob3 = f"https://islomuz.herokuapp.com/api/savol/{uch}"
    	re3 = requests.get(javob3).json()
    	savolnomi3 = (re3["title"])
    	savolvaqti3 = (re3["quest_time"])
    	savoli3 = (re3["question_text"])
    	javobi3 = (re3["answer_text"])
    	await message.reply(f"<b>📕 Савол номи - {savolnomi3}\n⏰ Савол берилган вақти - {savolvaqti3}\n\n📝 Савол - {savoli3}\n\n📕 Савол Жавоби - {javobi3}\n\n🌐Manba - Savollar.islom.uz\n🤖Bot - @islom_namoz_bot</b>")
    except:
    	pass
    try:
    	tort = (r["results"]["4"]["quest_id"])
    	javob4 = f"https://islomuz.herokuapp.com/api/savol/{tort}"
    	re4 = requests.get(javob4).json()
    	savolnomi4 = (re4["title"])
    	savolvaqti4 = (re4["quest_time"])
    	savoli4 = (re4["question_text"])
    	javobi4 = (re4["answer_text"])
    	await message.reply(f"<b>📘 Савол номи - {savolnomi4}\n⏰ Савол берилган вақти - {savolvaqti4}\n\n📝 Савол - {savoli4}\n\n📕 Савол Жавоби - {javobi4}\n\n🌐Manba - Savollar.islom.uz\n🤖Bot - @islom_namoz_bot</b>")
    except:
    	pass
    try:
    	besh = (r["results"]["5"]["quest_id"])
    	javob5 = f"https://islomuz.herokuapp.com/api/savol/{besh}"
    	re5 = requests.get(javob5).json()
    	savolnomi5 = (re5["title"])
    	savolvaqti5 = (re5["quest_time"])
    	savoli5 = (re5["question_text"])
    	javobi5 = (re5["answer_text"])
    	await message.reply(f"<b>📙 Савол номи - {savolnomi5}\n⏰ Савол берилган вақти - {savolvaqti5}\n\n📝 Савол - {savoli5}\n\n📕 Савол Жавоби - {javobi5}\n\n🌐Manba - Savollar.islom.uz\n🤖Bot - @islom_namoz_bot</b>")
    	await message.answer("<b>📇 Quydagi Savollar va Javoblarni o'qib chiqing va Savolingizga Javob topasiz degan ummidamiz😊</b>")
    except:
    	pass