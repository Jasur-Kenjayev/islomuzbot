from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

poklan = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚿 G‘usl"),
        ],
       [
       	KeyboardButton(text="💧Tahorat"),
       	KeyboardButton(text="🏜 Tayammum"),
       ],
      [
       	KeyboardButton(text="◀️ Orqaga"),
        ],
    ],
    resize_keyboard=True,
)