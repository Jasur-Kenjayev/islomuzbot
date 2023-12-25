from aiogram import types
from loader import dp, bot
from aiogram.types import Message

@dp.message_handler(text="🌆 Bomdod")
async def namoz_bomdoda(message: Message):
    videobomdoda = "BAACAgIAAxkBAAIHmmIXWaCfzPSuNldEryFsKH33YpW3AAL-EgACDxaBS5HjDNIHuJ_cIwQ"
    await message.answer_video(videobomdoda, caption=f"<b>🌆 Bomdod namozini to'liq o'qish tartibi (Ayollar uchun)\n\n✅ @islom_namoz_bot</b>")
    
    
@dp.message_handler(text="🏙 Peshin")
async def namoz_peshina(message: Message):
    videopeshina = "BAACAgIAAxkBAAIHnGIXWaa0AhOwGMcC2BngBUDbOgKTAAKgFQACxmr5S0V_74ESQFHaIwQ"
    await message.answer_video(videopeshina, caption=f"<b>🏙 Peshin namozini to'liq o'qish tartibi (Ayollar uchun)\n\n✅ @islom_namoz_bot</b>")
    
    
@dp.message_handler(text="🌅 Asr")
async def namoz_asra(message: Message):
    videoasra = "BAACAgIAAxkBAAIHnmIXWa0joNDP05deLpEVsrNu99Y4AALHGwACq1n5S7luMQZr4yxvIwQ"
    await message.answer_video(videoasra, caption=f"<b>🌅 Asr namozini to'liq o'qish tartibi (Ayollar uchun)\n\n✅ @islom_namoz_bot</b>")
    
    
@dp.message_handler(text="🌉 Shom")
async def namoz_shoma(message: Message):
    videoshoma = "BAACAgIAAxkBAAIHoGIXWbPs2MsVjSaXButYydq1Mm2DAALtFgACKvXxSx8kdyaz_AENIwQ"
    await message.answer_video(videoshoma, caption=f"<b>🌉 Shom namozini to'liq o'qish tartibi (Ayollar uchun)\n\n✅ @islom_namoz_bot</b>")
    
    
@dp.message_handler(text="🌃 Xufton va Vitr")
async def namoz_huftona(message: Message):
    videohuftona = "BAACAgIAAxkBAAIHomIXWbkeHp0sBmDgp7NGNb7_ZpzSAAIzGQACgnCBSkkpTJYGZ9P1IwQ"
    await message.answer_video(videohuftona, caption=f"<b>🌃 Xufton va Vitr namozini to'liq o'qish tartibi (Ayollar uchun)\n\n✅ @islom_namoz_bot</b>")
