import telebot

def tele_list():
    token='6533331762:AAHTH8lh2vl8WOYtFuKCs5HBmPXaIZeEFXY'
    bot=telebot.TeleBot(token)
    chat_id='1366665116'
    with open('to_do_new.txt', 'r') as f:
        file = f.read()
        #print(file)
    bot.send_message(chat_id,file)


def tele_rem(txt):
    token = '6533331762:AAHTH8lh2vl8WOYtFuKCs5HBmPXaIZeEFXY'
    bot = telebot.TeleBot(token)
    chat_id = '1366665116'
    bot.send_message(chat_id, txt)