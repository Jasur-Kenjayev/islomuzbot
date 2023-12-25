from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Quronm = ReplyKeyboardMarkup(
    keyboard=[
        [
       	KeyboardButton(text="📖 Qur'on Audio (🇸🇦 Arabcha)"),
       ],
       [
       	KeyboardButton(text="📖 Qur'on Audio (🇺🇿 O'zbekcha)"),
       ],
       [
       	KeyboardButton(text="Orqaga ▶️"),
        ],
    ],
    resize_keyboard=True,
)