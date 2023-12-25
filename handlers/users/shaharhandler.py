import logging
from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.shahar import orqaga
from keyboards.inline.menuin import categoryMenu
import requests
import json
import datetime
import pytz

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.answer(f"<b>🕌 Marhamat kerakli viloyatni Tanlang!</b>",reply_markup=categoryMenu)
    await call.message.delete()

def soat():
	utc_now = pytz.utc.localize(datetime.datetime.utcnow())
	pst_now = utc_now.astimezone(pytz.timezone("Asia/Tashkent"))
	dt_string = pst_now.strftime("%d.%m.%Y-YIL\n⏰ Soat - %H:%M:%S")
	return dt_string
	
@dp.callback_query_handler(text="27")
async def toshkent(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/27'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Toshkent Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="43")
async def toshkent1(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/43'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Angren Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="2")
async def toshkent2(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/2'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Bekobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
 
@dp.callback_query_handler(text="1")
async def andjon(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/1'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Andijon Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="31")
async def andjon2(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/31'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Xonobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="28")
async def andjon3(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/28'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Shahrixon Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="29")
async def andjon4(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/29'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Xo'jaobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="37")
async def fargona(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/37'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Farg'ona Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="13")
async def fargona2(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/13'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Marg'ilon Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="26")
async def fargona3(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/26'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Qo'qon Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="39")
async def fargona4(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/39'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Rishton Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="38")
async def fargona5(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/38'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Oltiariq Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="40")
async def fargona6(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/40'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Quva Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="15")
async def namangan(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/15'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Namangan Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="35")
async def nma1(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/35'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Chortoq Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="33")
async def nma2(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/33'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Chust Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="32")
async def nma3(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/32'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Pop Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="36")
async def nmar4(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/36'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Uchqo'rg'on Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="5")
async def so1(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/5'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Guliston Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="49")
async def so2(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/49'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Paxtaobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="9")
async def jzz(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/9'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Jizzax Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="50")
async def jzz1(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/50'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Zomin Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="55")
async def jzzvb(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/55'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 G'allaorol Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="51")
async def jzz4(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/51'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Do'stlik Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="18")
async def sd(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/18'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Samarqand Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="11")
async def sd1(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/11'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Kattaqo'rg'on Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="72")
async def urgut(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/72'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Urgut Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="4")
async def buxoro(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/4'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Buxoro Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="46")
async def gazli(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/46'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Gazli Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="48")
async def qora(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/48'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Qorako'l Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
  
@dp.callback_query_handler(text="25")
async def qarshi(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/25'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Qarshi Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="84")
async def dexqon(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/84'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Dehqonobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="88")
async def muborak(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/88'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Muborak Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="85")
async def guzor(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/85'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 G'uzor Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="74")
async def termiz(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/74'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Termiz Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="76")
async def boysun(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/76'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Boysun Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="6")
async def dnov(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/6'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Denov Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="77")
async def sherao(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/77'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Sherobod Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="75")
async def qumqor(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/75'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Qumqo'rg'on Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="14")
async def navoiy(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/14'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Navoiy Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
  
@dp.callback_query_handler(text="59")
async def knemex(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/59'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Konimex Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="17")
async def nurota(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/17'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Nurota Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="63")
async def uzquk(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/63'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Uchquduq Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="78")
async def urganch(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/78'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Urganch Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="79")
async def xazod(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/79'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Xazorasp Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="80")
async def xonqa1(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/80'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Xonqa Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="82")
async def shavott(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/82'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Shovot Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="21")
async def xivao(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/21'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Xiva Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="16")
async def nukszli(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/16'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Nukus Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="68")
async def moyn(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/68'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Mo'ynoq Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
  
@dp.callback_query_handler(text="66")
async def ghjvhi(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/66'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Taxtako'pir Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="65")
async def yvvn(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/65'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 To'rtko'l Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="71")
async def mionak(call: CallbackQuery):
    url1 = f'https://islomuz.herokuapp.com/api/namoz/71'
    r = requests.get(url1).json()
    bomdod = (r['bomdod'])
    peshin = (r['peshin'])
    asr = (r['asr'])
    shom = (r['shom'])
    xufton = (r['xufton'])
    await call.message.answer(f"<b>🕌 Qo'ng'irot Shahri\n➖➖➖➖➖➖\n📆 Bugun - <b>{soat()}</b>\n➖➖➖➖➖➖\n🌆 Bomdod: {bomdod}\n🏙 Peshin: {peshin}\n🌅 Asr: {asr}\n🌉 Shom: {shom}\n🌃 Xufton: {xufton}\n➖➖➖➖➖➖\nℹ️ Malumot @islom_namoz_bot Tomonidan taqdim etildi!</b>",reply_markup=orqaga)
    await call.message.delete()
    await call.answer(cache_time=60)
soat()
    
    

    

	
	