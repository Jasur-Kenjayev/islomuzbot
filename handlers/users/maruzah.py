from aiogram.types import Message
from loader import dp

@dp.message_handler(text="Alloh eng yomon ko‘rgan narsa")
async def fun1(message: Message):
    video_id = "BAACAgQAAxkBAAIO0mIZ8fl3o0alTHI8l5FVExJQa7hlAAIdBwACncaxURGN59KujLauIwQ"
    await message.answer_video(video_id, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nAlloh eng yomon ko‘rgan narsa</b>")
    
@dp.message_handler(text="Din kimdan o‘rganiladi")
async def select_naozoqs1(message: Message):
    video_1 = "BAACAgIAAxkBAAIO1GIZ8g3cPCUH6gw16gH1iVY7_iEdAALHEQACoR2oSvfBXbCuiFjYIwQ"
    await message.answer_video(video_1, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nDin kimdan o‘rganiladi</b>")
    
@dp.message_handler(text="Ahli kitob bilan bo‘ladigan munosabat")
async def select_naozoqs2(message: Message):
    video_2 = "BAACAgQAAxkBAAIO1mIZ8ihSKgWB4JgcoBekravh_w3hAAKABgACz2hgUvx8icDDcMPTIwQ"
    await message.answer_video(video_2, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nAhli kitob bilan bo‘ladigan munosabat </b>")
    
@dp.message_handler(text="Nega ishimiz yurishmayabdi")
async def select_naozoqs3(message: Message):
    video_3 = "BAACAgQAAxkBAAIO2GIZ8j5uhFGMe1wLW4HRybXjYizPAAIXBgACum6ZUSyDEKYEzszDIwQ"
    await message.answer_video(video_3, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nNega ishimiz yurishmayabdi</b>")
    
@dp.message_handler(text="Mulk surasining mo‘jizasi")
async def select_naozoqs4(message: Message):
    video_4 = "BAACAgQAAxkBAAIO2mIZ8k4nT5I3m1uEEVNVs6nRvH2eAAJjBgACnjvYUEqMB04_AZrGIwQ"
    await message.answer_video(video_4, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nMulk surasining mo‘jizasi</b>")
    
@dp.message_handler(text="Oila ajralishi sababi")
async def select_naozoqs5(message: Message):
    video_5 = "BAACAgQAAxkBAAIO3GIZ8mOgTr6VksCHySYrwshrTTkHAAJyBQACwWDoUxSTbxUpLt2LIwQ"
    await message.answer_video(video_5, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nViloyatlardagi oilalar ajralishi sababi</b>")
    
@dp.message_handler(text="Ajralishuvlar ko‘paysa nima qilinadi")
async def select_naozoqs6(message: Message):
    video_6 = "BAACAgQAAxkBAAIO3mIZ8nQhl1Z-22b7FUgkSC19P9ZPAAKWBQAC5XwRUh4oiz5Xe1ZyIwQ"
    await message.answer_video(video_6, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nAjralishuvlar ko‘paysa nima qilinadi</b>")
    
@dp.message_handler(text="Oilani buzishga majburlashga ota-onaning haqqi yo‘q")
async def select_naozoqs7(message: Message):
    video_7 = "BAACAgQAAxkBAAIO4GIZ8nxPwiWw063ySXeAuK5MWWWcAALtDAAC1hbIUS1VKwXGc-xyIwQ"
    await message.answer_video(video_7, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nOilani buzishga majburlashga ota-onaning haqqi yo‘q</b>")
    
@dp.message_handler(text="Taloq nima degani")
async def select_naozoqs8(message: Message):
    video_8 = "BAACAgQAAxkBAAIO4mIZ8ohJXr6T-vU-lS3Ym2pAgIL2AAKbBgACUHHoUlL-M3xqbRiXIwQ"
    await message.answer_video(video_8, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nTaloq nima degani</b>")
    
@dp.message_handler(text="Taloq qachon ishlatiladi")
async def select_naozoqs9(message: Message):
    video_9 = "BAACAgQAAxkBAAIO5GIZ8oy2Hv6p-l6g5NLqSr-1ULowAAKLBQACnxE4UquQXZp9MjaKIwQ"
    await message.answer_video(video_9, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nTaloq qachon ishlatiladi</b>")
    
@dp.message_handler(text="Taloq qachon tushadi")
async def select_naozoqq10(message: Message):
    video_10 = "BAACAgQAAxkBAAIO5mIZ8pYs44jB4qUDE4lILug6roGeAAKmBQACqsvhUfSi_WwDSK1PIwQ"
    await message.answer_video(video_10, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nTaloq qachon tushadi</b>")
    
@dp.message_handler(text="Xotinni taloq bilan qo‘rqitish-nomardlik")
async def select_naozoqs11(message: Message):
    video_11 = "BAACAgQAAxkBAAIO6GIZ8pyao36geKENFYEgPv4BmyTJAALqBAACS01ZUuihzCsLVdvRIwQ"
    await message.answer_video(video_11, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nEr o‘z xotinini taloq bilan qo‘rqitishi-nomardlikdir</b>")
    
@dp.message_handler(text="Folbinlik")
async def select_naozoq12(message: Message):
    video_12 = "BAACAgQAAxkBAAIO6mIZ8qBdxJ0v1v09a2yhV03lUBV2AAJMBgACP07gUk0x3rIvVAL7IwQ"
    await message.answer_video(video_12, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nFolbinlik shariatga xilof, iymonga xilof, musulmonchilikga xilof</b>")
    
@dp.message_handler(text="Kim folbinga borsa")
async def select_naozoqs13(message: Message):
    video_13 = "BAACAgQAAxkBAAIO7GIZ8qY5kXMR-1n7M7zvxrzTZmToAALmBgACM195UCu_NeOnhlxXIwQ"
    await message.answer_video(video_13, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nKimki folbinga borsa</b>")
    
@dp.message_handler(text="Folbinga ishonuvchilar")
async def select_naozoqs14(message: Message):
    video_14 = "BAACAgQAAxkBAAIO7mIZ8q0HQ02ajk91CFTxX9dpjyJDAAISBgAC44lYU4etF8S5IDxIIwQ"
    await message.answer_video(video_14, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nMusulmonman deganlar orasidan folbinlar, folbinga ishonuvchilar chiqdi</b>")
    
@dp.message_handler(text="Folbinlik-kufrdir")
async def select_naozoqs15(message: Message):
    video_15 = "BAACAgQAAxkBAAIO8GIZ8rGUkq1vioCY4Z-JiEwwLrLHAAKUCAACu405Uz6v-ae0gYxqIwQ"
    await message.answer_video(video_15, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nFolbinlik bu kufr</b>")
    
@dp.message_handler(text="Abror Muxtor Aliy Folbinlar Haqida")
async def barormux(message: Message):
    videoab = "BAACAgIAAxkBAAIPB2IaAZ4Vv7z7yt6yafWeT--XOtUkAAIqFAACixHRSPpAs0IXX3ltIwQ"
    await message.answer_video(videoab, caption=f"<b>Abror Muxtor Aliy Folbinlar Haqida!!!</b>")
    
@dp.message_handler(text="Safar namozi haqida")
async def select_naozoqs16(message: Message):
    video_16 = "BAACAgQAAxkBAAIO8mIZ8sUUgtAaAwyRt-G0kIPQcNHGAAIuBwACXFnhUML6a-MtNOzVIwQ"
    await message.answer_video(video_16, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nSafar namozi haqida batafsil</b>")
    
@dp.message_handler(text="Kibr Haqida")
async def select_naozoqs17(message: Message):
    video_17 = "BAACAgIAAxkBAAIO9GIZ8tsP0FvXpRWk3hKEWhooL7LMAAIOFwACllLRSG-pckamM6LzIwQ"
    await message.answer_video(video_17, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf\n\nKibr Haqida</b>")
    
@dp.message_handler(text="Poraxo'rlik")
async def select_naozoqs18(message: Message):
    video_18 = "BAACAgIAAxkBAAIO9mIZ8uo7Bflmc_-EUbC3ZWXbB8avAAJSEwACixHRSIDMuMRIUUcDIwQ"
    await message.answer_video(video_18, caption=f"<b>KORRUPSIYA-PORAXO'RLIK HAQIDA Abror Muxtor Aliy  </b>")
    
@dp.message_handler(text="Qimor o'ynash")
async def select_naozoqs19(message: Message):
    video_19 = "BAACAgIAAxkBAAIO-GIZ8vmgMYu-99ygZZ98qf4xSIqZAALhFAACYWsAAUj6n46lyUTjCiME"
    await message.answer_video(video_19, caption=f"<b>Abror Muxtor Aliy\n\nQimor haqida</b>")
    
@dp.message_handler(text="Yolg'on gapirish")
async def select_naozoqs20(message: Message):
    video_20 = "BAACAgIAAxkBAAIO-mIZ8wj5sUdAj8-EkEnUpRNO6GfZAAJOEwACixHRSOe5JLpHsY9EIwQ"
    await message.answer_video(video_20, caption=f"<b>Shayx Muhammad Sodiq Muhammad Yusuf - Yolg'on gapirish haqida</b>")
    
@dp.message_handler(text="Zino Haqida")
async def select_naozoqs21(message: Message):
    video_21 = "BAACAgIAAxkBAAIO_GIZ8xg41KmVLHHy-irw6Jh6LT8ZAAIgEwACixHRSHmVXTidcIYkIwQ"
    await message.answer_video(video_21, caption=f"<b>Abror Muxtor Aliy\n\nZino haqida</b>")
    
@dp.message_handler(text="sudxo'rlik haqida")
async def select_naozoqs22(message: Message):
    video_22 = "BAACAgIAAxkBAAIO_mIZ8yoe4MX8VJD2eyRK6AqfCww-AAIXEwACixHRSDovq0dpeqk6IwQ"
    await message.answer_video(video_22, caption=f"<b>sudxo'rlik haqida Shayx Muhammad Sodiq Muhammad Yusuf rohimahulloh</b>")
    
@dp.message_handler(text="Qanday Qizga Uylansa bo'ladi")
async def select_naozoqs23(message: Message):
    video_23 = "BAACAgIAAxkBAAIPA2IaAZOdaYtqlw2xIevRG_aGBksiAAITFAACixHRSDRCRlCd0opNIwQ"
    await message.answer_video(video_23, caption=f"<b>Bo'ydoqlarga Nasixat. Qanday qizga uylansa boladi? Abror Muxtor Aliy</b>")
    
    
    