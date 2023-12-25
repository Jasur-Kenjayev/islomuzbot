from keyboards.default.namozm import Namozm
from keyboards.default.menu import Menu
from keyboards.default.namozjamo import Namojamo
from keyboards.default.namozjanaza import Namozjan
from keyboards.default.poklanish import poklan 
from keyboards.default.foydali import Foydali, Savol
from keyboards.default.quronm import Quronm
from keyboards.default.quron import Quron
from keyboards.default.quranuz import Quranuz
from keyboards.default.beshfarz import Beshfarz
from keyboards.default.maruza import Maruza
from keyboards.default.allahningismlari import Allahningismlari
from keyboards.default.namozerkak import Namozerkak 
from keyboards.default.namozayol import Namozayol 
from loader import dp
from aiogram.types import Message

	
@dp.message_handler(text="🕌 Namoz")
async def select_naozoqs(message: Message):
    photo_id = "AgACAgIAAxkBAAIHAAFiF0R6-UHJN8lBD2QZNgXsYGUvmwACLL0xG4SRuUi1Wk52WaBF1AEAAwIAA3kAAyME"
    await message.answer_photo(photo_id, caption=f"<b>🕌 Namoz Bo'lmidasiz.\n\n📿 O'zizga Kerakli Bo'limni Tanlang.\n\n✅ @islom_namoz_bot</b>",reply_markup=Namozm)
 
 
@dp.message_handler(text="👥 Jamoat Namozlari")
async def namoz_jamo(message: Message):
    photo_jamo = "AgACAgIAAxkBAAIH4WIXYBG0JMcldF2ARAJqqPA9ONlaAAKAvTEbhJG5SF_oniCsAdiWAQADAgADeQADIwQ"
    await message.answer_photo(photo_jamo, caption=f"<b>👥 Jamoat Namozlari Bo'lmidasiz. \n\n🧎‍♂ O'zizga Kerakli Bo'limni Tanlang.\n\n✅ @islom_namoz_bot</b>",reply_markup=Namojamo)


@dp.message_handler(text="⚰ Janoza Namozi")
async def namoz_janaza(message: Message):
    photo_jan = "AgACAgIAAxkBAAIH22IXX_979-10o3Ln54Wim31yjprhAAJWuTEbeta5SHEsuFRxFRIFAQADAgADeQADIwQ"
    await message.answer_photo(photo_jan, caption=f"<b>⚰ Janoza Namozi Bo'lmidasiz.\n\n⏳ O'zizga Kerakli Bo'limni Tanlang.\n\n✅ @islom_namoz_bot</b>",reply_markup=Namozjan)
    
    
@dp.message_handler(text="Orqaga ▶️")
async def select_namoz(message: Message):
    await message.answer(f"<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>", reply_markup=Menu)
    
    
@dp.message_handler(text="🛁 Poklanish")
async def poklanish(message: Message):
    photo_pok = "AgACAgIAAxkBAAIHJmIXUGNaeg4I5Y_UaZIsm44o4rWWAAI5uTEbeta5SCyoGHa11b7cAQADAgADbQADIwQ"
    await message.answer_photo(photo_pok, caption=f"<b>🛁 Poklanish Bo'lmidasiz. O'zizga Kerakli Bo'limni Tanlang.\n\n✅ @islom_namoz_bot</b>",reply_markup=poklan)
    
@dp.message_handler(text="📿 Foydali Bo'lim")
async def foydalib(message: Message):
    foydali_id = "AgACAgIAAxkBAAIQ7mIaUmlB9JW1ba8PI1Q05feFtSI9AAJcuDEb6tXZSGwdGt0sHXjrAQADAgADeAADIwQ"
    await message.answer_photo(foydali_id,caption="<b>🤖 Siz Foydali Bo'limdasiz\n\n📇 Marhamat Kerakli Menuni Tanlang\n\n✅ @islom_namoz_bot</b>", reply_markup=Foydali)
    
@dp.message_handler(text="📬 Savol Yo'llash")
async def savoli(message: Message):
    savoly = "AgACAgIAAxkBAAInZmIo3XPJYmXwxJTnXLRpK49zzLqiAAIlvjEb9URJSVZA3SuyopsxAQADAgADeAADIwQ"
    await message.answer_photo(savoly,caption="<b>🤖 Siz Savol Yo'llash bo'limidasiz\n\n📨 Marhamat Savol Turini Tanlang\n\n✅ @islom_namoz_bot</b>", reply_markup=Savol)
    
    
@dp.message_handler(text="📖 Qur‘on")
async def quranuz(message: Message):
    photo_quron = "AgACAgIAAxkBAAIMqGIYs3i9AAF-1m4dsTgfRFCSzTnaMAACVMAxG4SRyUiRGWOpJM-PrQEAAwIAA3kAAyME"
    await message.answer_photo(photo_quron, caption=f"<b>📖 Siz Qur'oni Karim Bo'limidasiz\n\n📒 Marxamat Kerakli Menuni Tanlang\n\n✅ @islom_namoz_bot</b>",reply_markup=Quronm)
    

@dp.message_handler(text="◀️ Orqaga")
async def select_namoz(message: Message):
    await message.answer(f"<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>", reply_markup=Namozm)
    

@dp.message_handler(text="🔚 Orqaga")
async def select_namzd(message: Message):
    await message.answer(f"<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>", reply_markup=Namojamo)
    
    
@dp.message_handler(text="📖 Qur'on Audio (🇸🇦 Arabcha)")
async def select_quronar(message: Message):
    photo_quronarba = "AgACAgIAAxkBAAIMx2IYxVOuGoF41nAoPQqvvEJbFP7BAAKowDEbhJHJSIhvhyoTBelAAQADAgADeQADIwQ"
    await message.answer_photo(photo_quronarba, caption=f"<b>📖 Ushbu Bo'limda Qur'oni Karim ning Arabcha Audio Formatini Yuklab Olishingiz Mumkun.\n\n🎙 Audio Muallifi - Mishariy Roshid Al-Afasiy\n\n✅ @islom_namoz_bot</b>",reply_markup=Quron)
    

@dp.message_handler(text="📖 Qur'on Audio (🇺🇿 O'zbekcha)")
async def select_quronuz(message: Message):
    photo_quronuzba = "AgACAgIAAxkBAAIMxWIYxUGt9gRSQHVg5UBq0jrNKuC_AAKnwDEbhJHJSIV6tLnaHbeRAQADAgADeQADIwQ"
    await message.answer_photo(photo_quronuzba, caption=f"<b>📖 Ushbu Bo'limda Qur'oni Karim ning O'zbekcha Audio Formatini Yuklab Olishingiz Mumkun.\n\n🎙 Audio Muallifi - Afzal Rafiqov\n\n✅ @islom_namoz_bot</b>",reply_markup=Quranuz)
    
    
@dp.message_handler(text="⬅️ Orqaga")
async def select_orqac(message: Message):
    await message.answer(f"<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>", reply_markup=Quronm)
    

@dp.message_handler(text="Orqaga ➡️")
async def select_ortu(message: Message):
    await message.answer(f"<b>🤖Orqaga Muvafaqiyatli qaytdingiz✅</b>", reply_markup=Foydali)
    

@dp.message_handler(text="5️⃣ Farz")
async def select_farz(message: Message):
    await message.answer(f"<b>5️⃣ Farz bo'limidasiz quyidagi menulardan brini tanlang👇</b>", reply_markup=Beshfarz)
   

@dp.message_handler(text="🕋 Allohning go‘zal ismlari")
async def allahningismlari(message: Message):
    await message.answer(f"<b>🕋 Allohning ismlari va Sifatlari!\n\n🌐 https://islom.uz/maqola/149\n\n✅ @islom_namoz_bot</b>", reply_markup=Allahningismlari)


@dp.message_handler(text="🧔‍♂ Namoz")
async def namoz_erkak(message: Message):
    photo_erk = "AgACAgIAAxkBAAIHBmIXSSns3n_fxO09wIe8yW9mFpRvAAJBvTEbhJG5SCHUjzICnNRfAQADAgADeAADIwQ"
    await message.answer_photo(photo_erk, caption=f"<b>🧔‍♂ Erkaklar namozi bo'lmidasiz.\n\n✅ Ushbu bo'limda 5⃣ vaqt Namoz o'qish o'rgatilgan\n\n✅ @islom_namoz_bot</b>",reply_markup=Namozerkak)


@dp.message_handler(text="🧕 Namoz")
async def namoz_ayol(message: Message):
    photo_ayo = "AgACAgIAAxkBAAIHBGIXSRF68Ry8o19Mm_uAPiO9O0_GAAJAvTEbhJG5SCdnV3LLc3pGAQADAgADeQADIwQ"
    await message.answer_photo(photo_ayo, caption=f"<b>🧕 Ayollar namozi bo'lmidasiz\n\n✅ Ushbu bo'limda 5⃣ vaqt Namoz o'qish o'rgatilgan\n\n✅ @islom_namoz_bot</b>",reply_markup=Namozayol)
    
    
@dp.message_handler(text="🕌 Juma Namozi")
async def namoz_juma(message: Message):
    await message.answer("<b>🕌 Juma Namozi\n\nhttps://telegra.ph/JUMA-NAMOZI-02-24</b>")
    

@dp.message_handler(text="🌜Hayit Namozi")
async def namoz_hayt(message: Message):
	await message.answer("<b>🌜Hayit Namozi\n\nhttps://telegra.ph/HAYIT-NAMOZI-02-24</b>")

@dp.message_handler(text="🧎‍♂Musofir Namozi")
async def namoz_musof(message: Message):
	await message.answer("<b>🧎‍♂Musofir Namozi\n\nhttps://telegra.ph/MUSOFIR-NAMOZI-02-24</b>")
	
@dp.message_handler(text="🪦 Janoza Namozi")
async def janaza_namozi(message: Message):
    await message.answer("<b>🪦 Janoza Namozi\n\nhttps://telegra.ph/JANOZA-NAMOZI-02-24</b>")
    

@dp.message_handler(text="🤲 Janoza Duolari")
async def janaza_duosi(message: Message):
    await message.answer("<b>🤲 Janoza Duolari\n\nhttps://telegra.ph/JANOZA-DUOLARI-02-24</b>")
    
@dp.message_handler(text="🎙 Ma'ruzalar")
async def Maruzalar(message: Message):
    maruza_id= "AgACAgIAAxkBAAIQm2IaSRYMbjZCGa5cvKYIX6SlwwmyAAI4uDEb6tXZSDMUfd1Vf9KAAQADAgADeAADIwQ"
    await message.answer_photo(maruza_id, caption="<b>🤖 Siz Maruzalar Bo'limidasiz \n\n📒 Marhamat O'zingizga Kerakli Mavzuni Tanlang👇\n\n✅ @islom_namoz_bot</b>",reply_markup=Maruza)
    
@dp.message_handler(text="6⃣ Diniy Kalima")
async def oltikalima(message: Message):
    await message.answer("<b>6⃣ Diniy Kalima\n\n📇 https://telegra.ph/6-diniy-kalima-02-26\n\n✅ @islom_namoz_bot</b>")