import telebot

#TOKEN = "5366141483:AAEiYvQgf_zeWHU6I4EVzgPMxILNTEAoGMY"

bot = telebot.TeleBot('5366141483:AAEiYvQgf_zeWHU6I4EVzgPMxILNTEAoGMY')

# @bot.message_handler(content_types=['voice'])
# def function_name(message: telebot.type.Message):
#     bot.send_message(message.chat.id, 'У тебя очень красивый голос')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")

bot.polling(none_stop=True)