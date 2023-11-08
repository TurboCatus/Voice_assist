import telebot

def tele_list():
    token='token'
    bot=telebot.TeleBot(token)
    chat_id='chatid'
    with open('to_do_new.txt', 'r') as f:
        file = f.read()
        #print(file)
    bot.send_message(chat_id,file)


def tele_rem(txt):
    token = 'token'
    bot = telebot.TeleBot(token)
    chat_id = 'chaid'
    bot.send_message(chat_id, txt)
