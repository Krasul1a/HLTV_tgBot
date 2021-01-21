import telebot
from sraper import  matchLive,connect,disconnect
from config import API_tg

bot = telebot.TeleBot(API_tg, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    n = connect()
    print(n)
    bot.send_message(message.chat.id, "connect")


@bot.message_handler(commands=['match'])
def send_welcome(message):
    connect()
    tScore = matchLive()
    Text=''
    for i in tScore:
        lists = i.text.split('\n')

        Text += f'⠀{" "*20}{lists[0]}\n⠀{" "*21}{lists[1]}\n{lists[2]} {lists[3]} : {lists[5]} {lists[4]}\n\n\n'
    bot.send_message(message.chat.id, Text)
    disconnect()

bot.polling()