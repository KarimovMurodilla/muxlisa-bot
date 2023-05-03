from aiogram import types


def categories():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Biznes")
    btn2 = types.KeyboardButton("Sport")
    btn3 = types.KeyboardButton("Ta'lim")
    btn4 = types.KeyboardButton("Oziq-ovqat")
    btn5 = types.KeyboardButton("Boshqa")
    menu.add(btn1, btn2, btn3, btn4, btn5)

    return menu


def cancel():
    menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
    stop = types.KeyboardButton("Bekor qilish ❌")
    menu.add(stop)

    return menu