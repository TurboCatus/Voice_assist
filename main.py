import sys
import webbrowser
import speech_recognition as sr
import os
import pyaudio
import speech_recognition as speech_recog
import queue
import sounddevice as sd
import time
import requests
from datetime import datetime
import voice_file
import threading
#from threading import Thread
import vlc
import wake_up_clock
import listus
import subprocess
import omegaconf
import importlib
import Telegr
import reminder
#import Face_recog
import int_chat
import winsound


#webbrowser.register('firefox',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Mozilla Firefox\\firefox.exe'))


#-------------------------------------------------------------------------------------------
def speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-нибудь")
        audio = r.listen(source,phrase_time_limit=4,timeout=None)
    try:
        txt=r.recognize_google(audio, language="ru-RU")#show_all=True
        print(txt)
        if audio == None:
            print('0')
    except sr.UnknownValueError:
        #voice_file.speek("Робот не расслышал фразу")
        print(datetime.now(),"Робот не расслышал фразу")
    except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))
        txt = speech()
    return txt
#----------------------------------------------------------------------------------------------------
def rem_check():
    #reminder.reminder_check()
    voice_file.speek('Напоминание активировано'+reminder.reminder_check())
    Telegr.tele_rem(reminder.reminder_check())
    importlib.reload(reminder)
threading.Thread(target=rem_check).start()
'''
def fce_rcg():
    while True:
        import Face_recog
        if Face_recog.face_dec() == 'Match':
            voice_file.speek('Здраствуйте')

        time.sleep(5)
        importlib.reload(Face_recog)

threading.Thread(target=fce_rcg).start()
'''

#------------------------------------------------------------------------------------------------------
def do_it(txt):
    if 'плеер' in txt:
        os.startfile('vlc')
        
    #elif 'закрыть' in txt:
        #os.system('pkill vlc')
    
    elif 'открыть Google' in txt:
        url='https://google.com'
        webbrowser.open_new_tab(url)
        
    elif 'Google' in txt:
        print('What we search?')
        voice_file.speek('Что ищем?')
        url=speech()
        webbrowser.open_new_tab(f'https://www.google.com/search?q=+{url}')
        
    elif 'время' in txt:
        print(datetime.now().strftime('%H:%M:%S'))
        #time.sleep(2)
        voice_file.speek(voice_file.Time_to())
        
    elif 'дата' in txt:
        print(datetime.now().date())
        #time.sleep(2)

    elif 'прогноз погоды' in txt:
        voice_file.speek('Скажите город.')
        print('In what sity?')
        city=speech()
        response = requests.get(f'https://wttr.in/{city}')
        webbrowser.open_new_tab(f'https://wttr.in/{city}')
        print(response.text)
        

        #-- Либо открыть в новой вкладке
    elif 'погода' in txt:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        #def weth_1():
            #voice_file.speek(voice_file.Temperature())
        #def sp():
            #voice_file.speek('По данным другого источника.')
        def weth_2():
            voice_file.speek(voice_file.Temperature_sec())
        def winder():
            voice_file.speek(voice_file.wind())
           
        #weth_1()

        threading.Thread(target=weth_2).start()
        threading.Thread(target=winder).start()
        '''
        thr_1=Thread(target=weth_2)
        thr_2=Thread(target=winder)
        #thr_3=Thread(target=sp)
        thr_1.start()
        thr_2.start()
        #thr_3.start()
        thr_1.join()
        thr_2.join
        #thr_3.join
        '''
    elif 'таймер' in txt:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        def tmr():
            time.sleep(1)  # new
            voice_file.speek('На сколько?')
            tm=int(speech())*60
            song_tm=vlc.MediaPlayer('timer.mp3')
            while tm !=0:
                tm=tm-1
                time.sleep(1)
                print(tm)
            voice_file.speek('Таймер вышел')
            song_tm.play()
        threading.Thread(target=tmr).start()

    elif 'терминал' in txt:
        os.popen('cmd')

    elif 'YouTube' in txt:
        webbrowser.open_new_tab('https://youtube.com')

    elif 'найти видео' in txt:
        voice_file.speek('Какое видео ищем?')
        url_v=speech()
        webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={url_v}')

    elif 'будильник' in txt:
        #import wake_up_clock
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        importlib.reload(wake_up_clock)
        def alarm():
            voice_file.speek('готово')
            wake_up_clock.wake_up()
        threading.Thread(target=alarm).start()


    elif 'список' in txt:
        voice_file.speek('Записываю')
        def todo():
          fl=open('to_do.txt','w')
          i=0
          wrd=1
          while True:#i!=5 or wrd !='конец':
            wrd=speech()
            listus.wr(wrd)
            i=i+1
            print(i)
#            voice_file.speek('Что еще?')
            if i==10 or wrd == 'конец':
                voice_file.speek('Закрываю лист.')
                break
            voice_file.speek('Что еще?')
          fl.close()
          os.system('copy to_do.txt to_do_new.txt')
          Telegr.tele_list()
        thr_3=threading.Thread(target=todo)
        thr_3.start()
        thr_3.join()

    elif 'включить радио' in txt:
        def radio():
            subprocess.call('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe http://mp3.amgradio.ru/DeepFM')
        threading.Thread(target=radio).start()

    elif 'выключить радио' in txt:
        os.system('taskkill /IM vlc.exe')

    elif 'напоминание' in txt:
        #import reminder
        voice_file.speek('Скажите время:')
        tme = speech()
        time.sleep(2)
        voice_file.speek('Скажите дату:')
        dte = speech()
        time.sleep(2)
        voice_file.speek('О чем напомнить?')
        what = speech()
        time.sleep(1)
        reminder.reminder(tme,dte,what)
        importlib.reload(reminder) #----28.10


    elif 'стоп машина' in txt:
        time.sleep(30)
        
        #-- Стоп программы
    elif 'Завершить' in txt:
        sys.exit()
        exit()
        os.system('taskkill /IM main.exe') # new 11/09

    else :
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        #voice_file.speek('О чем вы хотели спросить?')
        def chat():
            int_chat.chat_wrt(txt)
        threading.Thread(target=chat).start()

#------------------------------------------------------------------------------------------------
while True:
    try:
        #do_it(speech_vosk())
        do_it(speech())
    except UnboundLocalError:
        pass
    except ConnectionResetError:
        pass
    #except:
        #pass



'''
while True:
    try:
        req = requests.get('https://google.com')
        if req.status_code == 200:
            do_it(speech())
        else:
            do_it(speech_vosk())
    except UnboundLocalError:
        pass
'''

