import telebot
from telebot import types

bot = telebot.TeleBot('6868538420:AAGyIp5u7ASEXWIttkuinc9bSI6__OhR2u0')


@bot.message_handler(commands=['start'])
def start(message):
        bot.send_message(message.from_user.id, 'Привет, я бот!')
        bot.send_message(message.from_user.id, "Для того, чтобы получть список команд \n"
                         "Напиши '/com'")


#кнопки в боте
@bot.message_handler(commands=['com'])
def com(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton(text="New_Task")
    button_2 = types.KeyboardButton(text='All_Tasks')
    keyboard.add(button_1, button_2)
    com_help = 'Держи список комманд! Если ты хочешь получить справку по командам, то вызови команду "/com_help"'
    bot.send_message(message.from_user.id, text=com_help, reply_markup=keyboard)


# метод проходит по алгоритму добавления задачи.
@bot.message_handler(text=['New_Task'])
def new_task(message):
     pass


@bot.message_handler(commands=['com_help'])
def com_help(message):
    help_message = f"Держи описание команд ;)\n""\nNew_Task - Это команда создает новую задачу и записывает ее, чтобы потом напомнить о ней.\n""\nAll_Tasks - Команда, которая выводит список всех текущих задач, которые ты записал."
    bot.send_message(message.from_user.id, text=help_message)


bot.polling()
