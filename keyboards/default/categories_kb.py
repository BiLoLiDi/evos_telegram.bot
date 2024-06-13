from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


def make_categories_kb(cart_exsist = False):
    categories = db.get_all_category()
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []
    for category in categories:
        buttons.append(
            KeyboardButton(text=category[-1])
        )

    menu.add(*buttons)
    menu.add(
        KeyboardButton(text="⬅️ Ortga")
    )
    return menu
