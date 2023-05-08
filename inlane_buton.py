from aiogram import Bot,Dispatcher, types, executor
import logging
import string
import random

from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from button_bot import rkm, rkm_in, ikm

API_TOKEN = "6272745530:AAEzFpIYlxnFM84Ocq4sgaVHAPv8d4scCMg"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


HELP_COMMAND = """
<b>/start</b> - <em>Botni ishga tushirish</em>
<b>/help</b> - <em>Yordam olish</em>
<b>/description</b> - <em>Bot haqida malumot olish</em>
<b>/photo</b> - <em>Rasm olish</em>
"""

description_flags = """
<b>/uzbekistan</b> - <em>aholisi: 36 024 946 kishi, maydoni: 448,9 ming kv. km, pul birligi: sum</em>
<b>/azrbaijan</b> - <em>aholisi: 9,5 mln. kishi, maydoni: 86,6 ming km², pul birligi: manat</em>
<b>/amerika</b> - <em>aholisi: 331 million kishi, maydoni: 9.8 million km², pul birligi: dollar</em>
<b>/turkiya</b> - <em>aholisi: 84.680.273 kishi, maydoni: 783,562 km², pul birligi: lira</em>
<b>/xitoy</b> - <em>aholisi: 1 mlrd. 394mln kishi, maydoni: 9,6 mln. km², pul birligi: yuan</em>
<b>/rassiya</b> - <em>aholisi: 145,3 mln kishi, maydoni:17,1 mln. km² kishi, pul birligi: rubl</em>
"""


PHOTOS_URL = [
    "https://www.istockphoto.com/photo/flag-of-uzbekistan-gm483290122-70560785?phrase=uzbekistan+flag",
    "https://www.istockphoto.com/photo/flag-of-azerbaijan-gm174951227-22265968?phrase=azerbaijan+flag",
    "https://www.istockphoto.com/vector/united-states-of-america-flag-gm1042208442-279027107?phrase=america+flag",
    "https://www.istockphoto.com/vector/turkish-flag-moon-and-star-with-red-background-gm1217770878-355594738",
    "https://uz.wikipedia.org/wiki/Xitoy_bayrog%CA%BBi#/media/Fayl:Chinese_flag_(Beijing)_-_IMG_1104.jpg",
    "https://www.istockphoto.com/photo/flag-of-russia-gm1127083981-296937553?phrase=russian+flag",
]


PHOTOS = dict(zip(PHOTOS_URL, ["uzbekistan", "azrbaijan", "amerika", "turkiya", "xitoy", "rassiya"]))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Salom botimizga hush kelibsiz",
                         reply_markup=rkm)


@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode="HTML")


@dp.message_handler(commands=['description'])
async def test(message: types.Message):
    await message.reply(text="<b>Bu botdan davlatlar haqida malumot olasiz</b>",
                        parse_mode="HTML")


@dp.message_handler(Text(equals="photo"))
async def photo_func(message: types.Message):
    await message.answer(text="Photo",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Random",
                         reply_markup=ikm)

@dp.message_handler(Text(['izoh']))
async def izoh_func(message: types.Message):
    await message.answer(text=description_flags,
                         parse_mode="HTML")




@dp.callback_query_handler()
async def callback_inline(callback: types.CallbackQuery):
    random_choice = random.choice(list(PHOTOS.keys()))
    if callback.data == "random":
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=random_choice,
                             caption=PHOTOS[random_choice],
                             reply_markup=ikm)
    elif callback.data == "back":
        await callback.message.answer(text="Back to home",
                                      reply_markup=rkm)


@dp.message_handler(commands=['manzili'])
async def loc(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=25.0756584,
                            longitude=54.8978298)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)

