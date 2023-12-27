import telebot
from telebot import types

bot = telebot.TeleBot('6868538420:AAGyIp5u7ASEXWIttkuinc9bSI6__OhR2u0')


@bot.message_handler(commands=['start'])
def start(message):
        bot.send_message(message.from_user.id, 'Привет, я таск-бот!')
        bot.send_message(message.from_user.id, "Для того, чтобы получть сисок команд \n"
                         "Напиши '/help'")


@bot.message_handler(commands=['help'])
def help(message):
        keyboard = types.ReplyKeyboardMarkup()
        key_new = types.KeyboardButton(text='Новая задача', callback_data='new_task')
        key_change = types.KeyboardButton(text='Внести измменения в задачу',
                                                callback_data='change_task')
        key_all = types.KeyboardButton(text='Показать все задачи', callback_data='all_tasks')
        keyboard.add(key_new, key_all, key_change)
        bot.send_message(message.from_user.id,text='Список доступных комманд:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'new_task':
        bot.send_message(call.message.chat.id, 'Запишу новую задачу')
    elif call.data == 'change_task':
        bot.send_message(call.message.chat.id, 'Измею текущую задачу')
    elif call.data == 'all_tasks':
        bot.send_message(call.message.chat.id, 'Покажу все существующие задачи')
    else:
         bot.send_messag(call.message.from_user.id, 'Я не понимаю, чего ты хочешь?!')


bot.polling()
