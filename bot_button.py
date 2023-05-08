from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

rkm = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="/start")
button2 = KeyboardButton(text="/help")
button3 = KeyboardButton(text="/description")
button4 = KeyboardButton(text="photo")
button5 = KeyboardButton(text="/location")
rkm.add(button, button2, button3, button4, button5)


rkm_in = ReplyKeyboardMarkup(resize_keyboard=True,
                             one_time_keyboard=True,
                             row_width=2)
btn = KeyboardButton(text="Random")
btn2 = KeyboardButton(text="Back")
rkm_in.add(btn, btn2)


ikm = InlineKeyboardMarkup(row_width=2)
ikm_button = InlineKeyboardButton(text="👍", callback_data="like")
ikm_button2 = InlineKeyboardButton(text="👎", callback_data="dislike")
ikm_button3 = InlineKeyboardButton(text="Random photo", callback_data="random")
ikm_button4 = InlineKeyboardButton(text="Back to Home", callback_data="back")

ikm.add(ikm_button, ikm_button2, ikm_button3, ikm_button4)