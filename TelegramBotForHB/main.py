import telebot
import time
from telebot import types
import random
import config
bot = telebot.TeleBot('6279231842:AAF0fLPqtyLs7SVJUVZ59PksLo7PRYEiHn4')
named_tuple = time.localtime()
time_string = time.strftime("%m/%d", named_tuple)
print(time_string)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Приветствую, я бот, который хранит подарок для самого лучшего папочки в мире! Для подробностей пиши /help")

    elif message.text == "/help":
        keyboard1 = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Подарок!', callback_data='Present')
        keyboard1.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Восспоминание!', callback_data='Life')
        keyboard1.add(key_no)
        bot.send_message(message.from_user.id, "В каком бы виде ты хотел получить подарок?", reply_markup=keyboard1)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    photos = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg',
              '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg',
              '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg', '30.jpg', '31.jpg']
    photosCopy = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg',
                  '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg',
                  '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg', '30.jpg', '31.jpg']

    if call.data == 'Present':
        named_tuple = time.localtime()
        time_string = time.strftime("%m/%d", named_tuple)
        if time_string == '03/09':
            keyboard = types.InlineKeyboardMarkup()
            key_yes = types.InlineKeyboardButton(text='Презентация!', callback_data='yes')
            keyboard.add(key_yes)
            key_no = types.InlineKeyboardButton(text='Фрагменты отправленные тебе сюда!', callback_data='no')
            keyboard.add(key_no)
            bot.send_message(call.message.chat.id, "В каком бы виде ты хотел получить подарок?", reply_markup=keyboard)
        else:
            bot.send_message(call.message.chat.id, "Если не время, значит не время")
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'https://disk.yandex.ru/d/S_YYeUMlh6d8Fw')
    if call.data == "no":

        photo1 = open('ScreenOfLife/1.jpg', 'rb')
        photo2 = open('ScreenOfLife/2.jpg', 'rb')
        photo3 = open('ScreenOfLife/3.jpg', 'rb')

        photo4 = open('ScreenOfLife/4.jpg', 'rb')
        photo5 = open('ScreenOfLife/5.jpg', 'rb')
        photo6 = open('ScreenOfLife/6.jpg', 'rb')

        photo7 = open('ScreenOfLife/7.jpg', 'rb')
        photo8 = open('ScreenOfLife/8.jpg', 'rb')
        photo9 = open('ScreenOfLife/9.jpg', 'rb')

        photo10 = open('ScreenOfLife/10.jpg', 'rb')

        photo11 = open('ScreenOfLife/11.jpg', 'rb')
        photo12 = open('ScreenOfLife/12.jpg', 'rb')
        photo13 = open('ScreenOfLife/13.jpg', 'rb')

        photo14 = open('ScreenOfLife/14.jpg', 'rb')
        photo15 = open('ScreenOfLife/15.jpg', 'rb')
        photo16 = open('ScreenOfLife/16.jpg', 'rb')

        photo17 = open('ScreenOfLife/17.jpg', 'rb')
        photo18 = open('ScreenOfLife/18.jpg', 'rb')
        photo19 = open('ScreenOfLife/19.jpg', 'rb')

        photo20 = open('ScreenOfLife/20.jpg', 'rb')
        photo21 = open('ScreenOfLife/21.jpg', 'rb')
        photo22 = open('ScreenOfLife/22.jpg', 'rb')
        photo23 = open('ScreenOfLife/23.jpg', 'rb')


        video1 = open('ScreenOfLife/24.3gp', 'rb')
        video2 = open('ScreenOfLife/25.3gp', 'rb')

        bot.send_message(call.message.chat.id, 'Самому лучшему папе посвещается!')
        for i in range(1, 6):
            time.sleep(1)
            bot.send_message(call.message.chat.id, f'{i}')

        bot.send_message(call.message.chat.id, 'В этот замечательный весенний день мы хотим пожелать тебе не терять настроения!')
        bot.send_photo(call.message.chat.id, photo1)
        bot.send_photo(call.message.chat.id, photo2)
        bot.send_photo(call.message.chat.id, photo3)
        time.sleep(4)

        bot.send_message(call.message.chat.id, 'Никогда не забывать, что мы всегда будем рядом и поможем!')
        bot.send_photo(call.message.chat.id, photo4)
        bot.send_photo(call.message.chat.id, photo5)
        bot.send_photo(call.message.chat.id, photo6)
        time.sleep(4)

        bot.send_message(call.message.chat.id, 'Спорт – это жыыыыызнь!')
        bot.send_photo(call.message.chat.id, photo7)
        bot.send_photo(call.message.chat.id, photo8)
        bot.send_photo(call.message.chat.id, photo9)
        time.sleep(4)

        bot.send_message(call.message.chat.id, 'Пост это конечно хорошо, нооо…')
        time.sleep(2)
        bot.send_photo(call.message.chat.id, photo10)
        time.sleep(4)

        bot.send_message(call.message.chat.id, 'Событие пройдет, но наслаждение от события – нет!')
        bot.send_photo(call.message.chat.id, photo11)
        bot.send_photo(call.message.chat.id, photo12)
        bot.send_photo(call.message.chat.id, photo13)
        time.sleep(4)

        bot.send_message(call.message.chat.id, 'Спасибо тебе за то, что ты у нас есть!')
        bot.send_photo(call.message.chat.id, photo14)
        bot.send_photo(call.message.chat.id, photo15)
        bot.send_photo(call.message.chat.id, photo16)
        time.sleep(4)


        bot.send_photo(call.message.chat.id, photo18)
        time.sleep(2)
        bot.send_photo(call.message.chat.id, photo19)
        time.sleep(2)
        bot.send_photo(call.message.chat.id, photo20)
        time.sleep(2)
        bot.send_photo(call.message.chat.id, photo21)
        time.sleep(2)
        bot.send_photo(call.message.chat.id, photo22)
        time.sleep(2)
        bot.send_photo(call.message.chat.id, photo23)
        time.sleep(2)

        bot.send_message(call.message.chat.id, 'С Днем Рождения!!')
        bot.send_video(call.message.chat.id, video1)
        time.sleep(3)
        bot.send_video(call.message.chat.id, video2)
    if call.data == 'Life':
        keyboard3 = types.InlineKeyboardMarkup()
        key_on = types.InlineKeyboardButton(text='Еще', callback_data='Life')
        keyboard3.add(key_on)
        rndm = random.choice(photos)
        photos.remove(rndm)
        photoMainLife = open(rndm, 'rb')
        bot.send_photo(call.message.chat.id, photoMainLife, reply_markup=keyboard3)
        if len(photos) == 0:
            keyboard4 = types.InlineKeyboardMarkup()
            key_yes2 = types.InlineKeyboardButton(text='Обнови!', callback_data='yes1')
            keyboard4.add(key_yes2)
            bot.send_messag e(call.message.chat.id, "Фотографии кончились, если хотите увидеть еще, то попросите разработчика добавить их. Я могу запустить эти фотографии еще раз, хотиет?", reply_markup=keyboard4)
    if call.data == 'yes1':
        photos = photosCopy
bot.polling(none_stop=True, interval=0)