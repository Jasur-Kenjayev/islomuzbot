from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳ Namoz vaqti"),
        ],
       [
       	KeyboardButton(text="🕌 Namoz"),
       	KeyboardButton(text="📖 Qur‘on"),
       ],
      [
      	KeyboardButton(text="📿 Foydali Bo'lim"),
       ],
    ],
    resize_keyboard=True,
)

bekor2 = ReplyKeyboardMarkup(
    keyboard = [
        [
        	KeyboardButton(text="↩️ Orqaga"),
        ],
     ],
     resize_keyboard=True
)

Savolb = ReplyKeyboardMarkup(
    keyboard = [
        [
        	KeyboardButton(text="📝 Savol Yuborish"),
        ],
        [
        	KeyboardButton(text="Orqaga ↪️"),
        ],
     ],
     resize_keyboard=True
)