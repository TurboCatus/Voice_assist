from aiogram import Bot, Dispatcher, executor, types
import os
import subprocess
import threading
import requests
import json


TOKEN = 'token'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def get_text_message(msg: types.Message):
    #await msg.answer(msg.text)
    if msg.text.lower() == 'привет':
        await  msg.answer('Hello')

    if msg.text.lower() == '1':
        await  msg.answer('Hello_commrads')

    if msg.text.lower() == 'лошадь':
        await  msg.answer('Плотва')

    if msg.text.lower() == 'vlc on':
        await msg.answer('VLC ON')
        def vlc_on():
            subprocess.call('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe http://mp3.amgradio.ru/DeepFM')
        threading.Thread(target=vlc_on).start()

    if msg.text.lower() == 'vlc off':
        await msg.answer('VLC OFF')
        def vlc_off():
            os.system('taskkill /IM vlc.exe')
        threading.Thread(target=vlc_off).start()

    if msg.text.lower() == 'погода':
        url = requests.get('https://api.open-meteo.com/v1/forecast?latitude=56.47&longitude=84.98&current_weather=true&windspeed_unit=ms&timezone=auto')
        tempr = url.text
        temp_js = json.loads(tempr)
        temp_di = temp_js.setdefault('current_weather')
        temp_val = temp_di.setdefault('temperature')
        temp_wind = temp_di.setdefault('windspeed')
        await msg.answer(f'Temp: {temp_val} \n Wind: {temp_wind}' )




    #else:
        #await  msg.answer('Dont understend')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)


