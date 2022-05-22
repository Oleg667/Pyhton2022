# OLEG18_667_bot.
import telebot

TOKEN = "5366141483:AAEiYvQgf_zeWHU6I4EVzgPMxILNTEAoGMY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Hello')

bot.polling()
