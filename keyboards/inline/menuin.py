from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🕌 Toshkent viloyati", callback_data="toshkent"),
        InlineKeyboardButton(text="🕌 Andijon viloyati", callback_data="andijon"),
    ],
    [
    	InlineKeyboardButton(text="🕌 Farg'ona viloyati", callback_data="fargona"),
        InlineKeyboardButton(text="🕌 Namangan viloyati", callback_data="namangan"),
    ],
    [
    	InlineKeyboardButton(text="🕌 Sirdaryo viloyati", callback_data="sirdaryo"),
        InlineKeyboardButton(text="🕌 Jizzax viloyati", callback_data="jizzax"),
    ],
    [
    	InlineKeyboardButton(text="🕌 Samarqand viloyati", callback_data="samarqand"),
        InlineKeyboardButton(text="🕌 Buxoro viloyati", callback_data="buxoro"),
    ],
    [
    	InlineKeyboardButton(text="🕌 Qashqadaryo viloyati", callback_data="qashqadaryo"),
        InlineKeyboardButton(text="🕌 Surxondaryo viloyati", callback_data="surxondaryo"),
    ],
    [
    InlineKeyboardButton(text="🕌 Navoiy viloyati", callback_data="navoiy"),
        InlineKeyboardButton(text="🕌 Xorazm viloyati", callback_data="xorazm"),
    ],
    [
    InlineKeyboardButton(text="🕌 Qoraqalpog'iston respublikasi", callback_data="qoraqalpogiston"),
    ],
])