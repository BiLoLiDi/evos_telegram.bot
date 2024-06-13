from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tel = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text = '📞Mening raqamim')
        ],
        [
            KeyboardButton(text = '⬅️Ortga')
        ]
    ]
)