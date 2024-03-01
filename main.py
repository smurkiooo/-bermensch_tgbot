import telebot
from telebot import types as tp
bot = telebot.TeleBot('7088109822:AAF6TpDbdcWrh2IkX41UGX6ogIFH23qcx7I')

@bot.message_handler(commands=['start'])
def start(message):
    markup = tp.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = tp.KeyboardButton("Deutsch")
    btn2 = tp.KeyboardButton("Englisch")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Wähle die Sprache", reply_markup=markup)

bot.polling(none_stop=True, interval=0)