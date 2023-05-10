import telebot
import time
from telebot import types
import random
import config
bot = telebot.TeleBot('') #Your token
named_tuple = time.localtime()
time_string = time.strftime("%m/%d", named_tuple)
print(time_string)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, " Yoir main text/help")

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
    photos = [''] #Your photos
    photosCopy = [''] #Your photos

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
        #for another photo u should create a new variable and paste them adress to the photo(for example upper)

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
            bot.send_message(call.message.chat.id, "Фотографии кончились, если хотите увидеть еще, то попросите разработчика добавить их. Я могу запустить эти фотографии еще раз, хотиет?", reply_markup=keyboard4)
    if call.data == 'yes1':
        photos = photosCopy
bot.polling(none_stop=True, interval=0)