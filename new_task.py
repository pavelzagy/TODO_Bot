import telebot
from telebot import types


class NewTask():
    def __init__(self, name, discription, file, deadline, reminder):
        self.name = ''
        self.discription = ''
        self.file = None
        self.deadline = ''  # Поставить дату в формате времени: или юникс или ИСО
        self.reminder = ''  # Поставить дату в формате времени: или юникс или ИСО


@bot.message_handler(text=['New_Task'])
def new_task(message):
    bot.send_message(message.from_user.id, 'Название задачи: ')
