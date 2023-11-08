import datetime
import os
import sys
import threading
import keyboard
import time
import vlc
import random


num_song=(random.randrange(1,10))
song=vlc.MediaPlayer(f'{num_song}.mp3')
##############################

with open ('alarm.txt','r') as f:
    alarm=f.read()

datat=datetime.datetime.now()
day_of_week=datetime.datetime.weekday(datat) #День недели в виде числа 0-Понедельник,1-Вторник
#Будильник заводится на день вперед.
#print('Day of week:',day_of_week)
for i, word in enumerate(alarm.splitlines(),0):
    #print(i,word)
    if i == day_of_week+1 and day_of_week <=5:
        print('Будильник заведен на:',word)
        spl=[j for j in word]
        #print(spl)
        if len(spl) > 6:  # Проверки на длину
            tmh_mnl = int(spl[2] + spl[3])
            # print(tmh_mnl)
            tmm_mnl = int(spl[5] + spl[6])
            # print(tmm_mnl)
        elif len(spl) == 6:
            tmh_mnl = int(spl[2])
            # print(tmh_mnl)
            tmm_mnl = int(spl[4] + spl[5])
            # print(tmm_mnl)
        else:
            print('Check alarm.txt')
    elif i == day_of_week-6 and day_of_week ==6:
        print(word)
        spl = [j for j in word]
        #print(spl)
        if len(spl) > 6:  # Проверки на длину
            tmh_mnl = int(spl[2] + spl[3])
            # print(tmh_mnl)
            tmm_mnl = int(spl[5] + spl[6])
            # print(tmm_mnl)
        elif len(spl) == 6:
            tmh_mnl = int(spl[2])
            # print(tmh_mnl)
            tmm_mnl = int(spl[4] + spl[5])
            # print(tmm_mnl)
        else:
            print('Check alarm.txt')
'''
tmh_mnl=20
tmm_mnl=30
'''
#Сравнение текущего времени с заданным
tme=5
IsAlive=True
#def wake_up():
def wake_up():
    #IsAlive=True
    #tme=5
    while IsAlive:
        #num_song = (random.randrange(1, 10))
        #song = vlc.MediaPlayer(f'{num_song}.mp3')
        dt=datetime.datetime.now()
        tmh=dt.hour #Hour, type=int
        tmm=dt.minute #Min, type=int
        #print(tm.hour,':',tm.minute)
        #if tmh == renew_alarm_h() and tmm == renew_alarm_m():
        if tmh == tmh_mnl and tmm == tmm_mnl:
            while IsAlive:
                print('Time to Wake UP')
                song.play()
                time.sleep(10)
                song.stop()
                time.sleep(tme)
        time.sleep(10) #---28.10

def wait():
    while True:
        global tme
        if keyboard.is_pressed('space'):
            tme=60
            time.sleep(30)
            tme=5
        if keyboard.is_pressed('q'):
            break

'''
#def total_stop():
#    while True:
#        global IsAlive
#        if keyboard.is_pressed('q'):
#            IsAlive = False
#            break
'''

def total_stop():
    while True:
        global IsAlive
        global wait
        if keyboard.is_pressed('q'):
            wait = False
            IsAlive = False
            sys.exit()


threading.Thread(target=wake_up).start()
threading.Thread(target=wait).start()
threading.Thread(target=total_stop).start()
#threading.Thread(target=renew_alarm).start()
#wake_up()




