import logging
from random import choice
from aiogram import os
from aiogram import Bot, Dispatcher, types, executor
from decouple import config

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 

API_TOKEN = '6415850890:AAGsIcLuCzJiaPlY0PpHewjHDqRr4m16G-4'

logging.basicConfig(level=logging.INFO)

bot = Bot(config('API_TOKEN'))
dp = Dispatcher(bot)

IMGS_PATH = 'IMG'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

key_word_photos = ['фото', 'малюнок', 'фотографія', 'фотографії', 'малюнки', 'малюнком', 'фотографією', 'фотографіям', 'малюнкам']

key_words = {'nature' : ['природа', 'природу', 'природі', '', '', '', ''] ,
             'people' : ['люди', 'людина', 'людей', 'людину', '', '', ''] ,
             'space' : ['космос', 'космосу', 'космоса', 'космосом', 'космосе', 'космосі', 'космосів', 'космосам', 'космосами'] 
}

@dp.message_handler(commands=['/start'])
async def send_welcome(message: types.Message):
    await message.answer('Привіт, це бот для отримання картинки за допомгою ключового слова.\n'
                        +'Напиши мені будь яке повідомлення з ключовими словами такі  як: Фото, космос, людина, природа')


def get_photo_by_key_word_photo(key_word_photo):
    path = f'{IMGS_PATH}/{key_word_photo}'
    files = os.lictdir(path)
    img = choice(files)
    return open(f'{path}/{img}', 'rb')

@dp.message_handler()
async def answers(message: types.Message):
    triger1 = False
    category = ''

    words = message.text.split( )

    for word in words:
        if word.lower() in key_word_photos:
            triger1 = True
            continue
        for key, value in key_words.items():
            if word.lower() in value:
                category = key
    if triger1 and category:
        await message.answer_photo(get_photo_by_key_word_photo(category))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)