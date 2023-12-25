from aiogram import types
from loader import dp, bot
from aiogram.types import Message

@dp.message_handler(text="🌖 Bomdod")
async def namoz_bomdod(message: Message):
    videobomdod = "BAACAgIAAxkBAAIHW2IXUvgjFQdA-qog3JKNl-PP-Y5CAALJFgACzPxASpx9XkocPXkyIwQ"
    await message.answer_video(videobomdod, caption=f"<b>🌖 Bomdod namozini to'liq o'qish tartibi (Erkaklar uchun)\n\n✅ @islom_namoz_bot</b>")
    
    
@dp.message_handler(text="☀️ Peshin")
async def namoz_peshin(message: Message):
    videopeshin = "BAACAgIAAxkBAAIHXWIXU0IvFiE4stcH-c6JIHFX7i0yAAIbFgAC1_lASnu1kaCUsuxzIwQ"
    await message.answer_video(videopeshin, caption=f"<b>☀️ Peshin namozini to'liq o'qish tartibi (Erkaklar uchun)\n\n✅ @islom_namoz_bot</b>")
    
    
@dp.message_handler(text="🌤 Asr")
async def namoz_asr(message: Message):
    videoasr = "BAACAgIAAxkBAAIHX2IXU1NQGVpb4UvcywPt6M80TogHAAJlFwACzPxASjeaf8mbjTGEIwQ"
    await message.answer_video(videoasr, caption=f"<b>🌤 Asr namozini to'liq o'qish tartibi (Erkaklar uchun)\n\n✅ @islom_namoz_bot</b>")
    
    
@dp.message_handler(text="🌥 Shom")
async def namoz_shom(message: Message):
    videoshom = "BAACAgIAAxkBAAIHYWIXU1o59Kyfdx7GooF4T97SrlyHAAIlEwAChH1ASnF5OKIkUgJuIwQ"
    await message.answer_video(videoshom, caption=f"<b>🌥 Shom namozini to'liq o'qish tartibi (Erkaklar uchun)\n\n✅ @islom_namoz_bot</b>")
    
    
@dp.message_handler(text="🌙 Hufton va Vitr")
async def namoz_hufton(message: Message):
    videohufton = "BAACAgIAAxkBAAIHY2IXU2D3FYCTRksiDqf54S_HA7DzAALBEgACmipgSgpkUgpH3vq3IwQ"
    await message.answer_video(videohufton, caption=f"<b>🌙 Hufton va Vitr namozini to'liq o'qish tartibi (Erkaklar uchun)\n\n✅ @islom_namoz_bot</b>")
