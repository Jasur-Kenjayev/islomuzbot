import logging
from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.inline.shahar import tashkenti, andjoni, farganai, namangani, sirdaryoi, jizzaxi, samarqandi, buxoroi, qashqadaryoi, surxondaryoi, navoiyi, xorazmi, qoraqalpogistoni
from keyboards.inline.menuin import categoryMenu
from aiogram.types import ParseMode, Message

@dp.message_handler(text_contains="⏳ Namoz vaqti")
async def select_category(message: Message):
    await message.answer(f"*⏰ Namoz vaqtlari Bo'limidasiz {message.from_user.full_name}\n\n🕌 Marhamat kerakli viloyatni Tanlang*",parse_mode=ParseMode.MARKDOWN, reply_markup=categoryMenu)

@dp.callback_query_handler(text="toshkent")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Toshkent viloyati shahridan birini tanlang!</b>", reply_markup=tashkenti)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="andijon")
async def buy_andijon(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Andijon viloyati shahridan birini tanlang!</b>", reply_markup=andjoni)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="fargona")
async def buy_fargona(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Farg'ona viloyati shahridan birini tanlang!</b>", reply_markup=farganai)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="namangan")
async def buy_namangan(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Namangan viloyati shahridan birini tanlang!</b>", reply_markup=namangani)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="sirdaryo")
async def buy_sirdaryo(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Sirdaryo viloyati shahridan birini tanlang!</b>", reply_markup=sirdaryoi)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="jizzax")
async def buy_jizzax(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Jizzax viloyati shahridan birini tanlang!</b>", reply_markup=jizzaxi)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="samarqand")
async def buy_samarqand(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Samarqand viloyati shahridan birini tanlang!</b>", reply_markup=samarqandi)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="buxoro")
async def buy_buxoro(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Buxoro viloyati shahridan birini tanlang!</b>", reply_markup=buxoroi)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="qashqadaryo")
async def buy_qashqadaryo(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Qashqadaryo viloyati shahridan birini tanlang!</b>", reply_markup=qashqadaryoi)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="surxondaryo")
async def buy_surxondaryo(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Surxondaryo viloyati shahridan birini tanlang!</b>", reply_markup=surxondaryoi)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="navoiy")
async def buy_navoiy(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Navoiy viloyati shahridan birini tanlang!</b>", reply_markup=navoiyi)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="xorazm")
async def buy_xorazm(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Xorazm viloyati shahridan birini tanlang!</b>", reply_markup=xorazmi)
    await call.answer(cache_time=60)
    
@dp.callback_query_handler(text="qoraqalpogiston")
async def buy_qoraqalpogiston(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🕌 Qoraqalpogiston viloyati shahridan birini tanlang!</b>", reply_markup=qoraqalpogistoni)
    await call.answer(cache_time=60)
    
    
