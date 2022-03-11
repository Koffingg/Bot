import re

import telebot
import markups as m
import random
from glob import glob

TOKEN = "5235302725:AAEyUNnoZ_HvcoyF1Ko8w_N6zRRJRUqO4xI"
bot = telebot.TeleBot(TOKEN)

with open('file_comp.txt', 'r') as file:
    lines = file.readlines()


@bot.message_handler(commands=['start'])
def start_bot(message):
    msg = bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} 👋, меня зовут KotikBot и вот что я умею:"
                                      f"\nОтправлять фото котиков",
                                      reply_markup=m.start_markup)
    bot.register_next_step_handler(msg, askPerson)


def askPerson(message):
    text = message.text.lower()
    if text == "давай котика":
        msg = bot.send_message(message.chat.id, 'Держи котика')
        lists = glob('images/*')
        picture = random.choice(lists)
        bot.send_photo(message.chat.id, photo=open(picture, 'rb'))
        bot.register_next_step_handler(msg, askPerson)

    elif text == "комплимент":
        msg = bot.send_message(message.chat.id, 'Держи комплимент', reply_markup=m.start_markup)
        line = random.choice(lines)
        bot.send_message(message.chat.id, line)
        bot.register_next_step_handler(msg, askPerson)

    elif text == "давай главную кису":
        msg = bot.send_message(message.chat.id, 'Посмотри, какая красивая!')
        lists = glob('im_kisa_boss/*')
        picture = random.choice(lists)
        bot.send_photo(message.chat.id, photo=open(picture, 'rb'))
        bot.register_next_step_handler(msg, askPerson)

    elif text == "давай главного котика":
        msg = bot.send_message(message.chat.id, 'Посмотри, какой красивый!')
        lists = glob('im_kotik_boss/*')
        picture = random.choice(lists)
        bot.send_photo(message.chat.id, photo=open(picture, 'rb'))
        bot.register_next_step_handler(msg, askPerson)

    elif text == "выключить":
        bot.send_message(message.chat.id, 'До скорой встречи!')
        return

    elif text == "перезапустить":
        msg = bot.send_message(message.chat.id, '/start')
        bot.register_next_step_handler(msg, start_bot)

    else:
        msg = bot.send_message(message.chat.id, 'Такой функции нет, повторите ввод.')
        bot.register_next_step_handler(msg, askPerson)


bot.polling(none_stop=True)
