from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Foydali = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🕋 Allohning go‘zal ismlari"),
        ],
       [
       	KeyboardButton(text="5️⃣ Farz"),
       	KeyboardButton(text="🎙 Ma'ruzalar"),
       ],
      [
      	KeyboardButton(text="🧭 Qibla Kompus"),
      	KeyboardButton(text="6⃣ Diniy Kalima"),
       ],
       [
       	KeyboardButton(text="🗞 Manbalar"),
       	KeyboardButton(text="📬 Savol Yo'llash"),
       ],
       [
       	KeyboardButton(text="Orqaga ▶️"),
        ],
    ],
    resize_keyboard=True,
)

Savol = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖 Dinimiz bo'yicha Savol"),
        ],
        [
        	KeyboardButton(text="🤖 Bot bo'yicha Savol"),
        ],
        [
        	KeyboardButton(text="Orqaga ➡️"),
        ],
    
    ],
    resize_keyboard=True,
)
        