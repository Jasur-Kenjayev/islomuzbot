from loader import dp
from aiogram.types import Message
from aiogram import types

@dp.message_handler(text="🚿 G‘usl")
async def select_gusl(message: Message):
    await message.answer("<b>🚿 G‘usl Haqida\n\n📇 https://telegra.ph/G%CA%BBUSL-02-23</b>")
    

@dp.message_handler(text="💧Tahorat")
async def select_taxorat(message: Message):
    await message.answer("<b>💧Tahorat Haqida\n\n📇 https://telegra.ph/Tahorat-haqida-02-23</b>")
    

@dp.message_handler(text="🏜 Tayammum")
async def select_tayamum(message: Message):
    await message.answer("<b>🏜 Tayammum\n\n📇 https://telegra.ph/Tayammum-haqida-02-23</b>")
 