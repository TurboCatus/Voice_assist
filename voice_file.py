import requests
import torch
import sounddevice as sd
import time
import numpy
from datetime import datetime
import json
import functools
import omegaconf

def Time_to():
#print(datetime.now().strftime('%H:%M'))
    Time=datetime.now().strftime('%H:%M')
#Time='01:30'
    hr={'01':'один час','02':'два часа','03':'три часа','04':'четыре часа','05':'пять часов','06':'шесть часов','07':'семи часов','08':'восемь часов','09':'девять часов','10':'десять часов',
        '11':'одиннадцать часов','12':'двенадцать часов','13':'тринадцать часов','14':'четырнадцать часов','15':'пятнадцать часов','16':'шестнадцать часов','17':'семнадцать часов',
        '18':'восемнадцать часов','19':'девятнадцать часов','20':'двадцать часов','21':'двадцать один час','22':'двадцать два часа','23':'двадцать три часа','00':'двадцать четыре часа'}
    min={'00':'ноль минут','01':'одна минута','02':'две минуты','03':'три минты','04':'четыре минуты','05':'пять минут','06':'шесть минут','07':'семь минут','08':'восемь минут','09':'девять минут',
        '10':'десять минут','11':'одиннадцать минут','12':'двенадцать минут','13':'тринадцать минут','14':'четырнадцать минут','15':'пятнадцать минут','16':'шестнадцать минут','17':'семнадцать минут',
        '18':'восемнадцать минут','19':'девятнадцать минут','20':'двадцать минту','21':'двадцать одна минута','22':'двадцать две минуты','23':'двадцать три минуты','24':'двадцать четыре минуты',
        '25':'двадцать пять минут','26':'двадцать шесть минут','27':'двадцать семь минут','28':'двадцать восемь минут','29':'двадцать девять минут','30':'тридцать минут','31':'тридцать одни минута',
        '32':'тридцать две минуты','33':'тридцать три минуты','34':'тридцать четыре минуты','35':'тридцать пять минут','36':'тридцать шесть минут','37':'тридцать семь минут','38':'тридцать восемь минут',
        '39':'тридцать девять минут','40':'сорок минут','41':'сорок одна минута','42':'сорок две минтуы','43':'сорок три минуты','44':'сорок четыре минтуы','45':'сорок пять минут','46':'сорок шесть минут',
        '47':'сорок семь минут','48':'сорок восемь минут','49':'сорок девять минут','50':'пятьдесят минут','51':'пятьдесят одна минута','52':'пятьдесят две минуты','53':'пятьдесят три минуты',
        '54':'пятьдесятчетыре минуты','55':'пятьдесятпять минут','56':'пятьдесят шесть минут','57':'пятьдесят семь минут','58':'пятьдесят восемь минут','59':'пятьдесят девять минут'}

    hrr=[]
    minn=[]
#-- Дробление часов на цифры и добавление в hrr
    sp=[i for i in Time]
    hrr.append(sp[0])
    hrr.append(sp[1])
    dj_hr=''.join(hrr)
#print(dj_hr)
#-- Дробление минут на цифры и добавление в hrr
    minn.append(sp[3])
    minn.append(sp[4])
    dj_min=''.join(minn)
#print(dj_min)
#-- Соединение часов и минут в список
    tm=[]
    tm.append(dj_hr)
    tm.append(dj_min)
#print(tm)
#print(hr.keys())
#print()
#-- Через цикл поиск ключа и запись значения в str_tm
    str_tm=[]

    for j in hr.keys():
    #print(j)
        if tm[0] == j:
        #print(hr.get(j))
            k_h=hr.get(j)
            str_tm.append(k_h)

    for q in min.keys():
    #print(q)
        if tm[1] == q:
        #print(min.get(q))
            k_m=min.get(q)
            str_tm.append(k_m)

#print(str_tm)
#-- Вывод времени в тестовом виде
    ss=str(','.join(str_tm))
    return ss
#print(ss)

#-- Температура за окном --#

def Temperature():
    sity='Новосибирск'
    Temper_s={'-':'минус'}
    Temper_num={'1':'один градус Цельсия','2':'два градуса Цельсия','3':'три градуса Цельсия','4':'четыре градуса Цельсия','5':'пять градусов Цельсия','6':'шесть градусов Цельсия','7':'семь градусов Цельсия','8':'восемь градусов Цельсия','9':'девять градусов Цельсия',
                '10':'десять градусов Цельсия','11':'одиннадцать градусов Цельсия','12':'двенадцать градусов Цельсия','13':'тринадцать градусов Цельсия','14':'четырнадцать градусов Цельсия','15':'пятнадцать градусов Цельсия','16':'шестнадцать градусов Цельсия',
                '17':'семнадцать градусов Цельсия','18':'восемнадцать градусов Цельсия','19':'девятнадцать градусов Цельсия','20':'двадцать градусов Цельсия','21':'двадцать один градус Цельсия','22':'двадцать два градуса Цельсия','23':'двадцать три градуса Цельсия',
                '24':'двадцать четыре градуса Цельсия','25':'двадцать пять градусов Цельсия','26':'двадцать шесть градуса Цельсия','27':'двадцать семь градусов Цельсия','28':'двадцать восемь градусов Цельсия','29':'двадцать девять градусов Цельсия',
                '30':'тридцать градусов Цельсия','31':'тридцать один градус Цельсия','32':'тридцать два градуса Цельсия','33':'тридцать три градуса Цельсия','34':'тридцать четыре градуса Цельсия','35':'тридцать пять градусов Цельсия','36':'тридцать шесть градусов Цельсия',
                '37':'тридцать семь градусов Цельсия','38':'тридцать восемь градусов Цельсия','39':'тридцать девят градусов Цельсия','40':'сорок градусов Цельсия','41':'сорок один градус Цельсия','42':'сорок два градуса Цельсия','43':'сорок три градуса Цельсия',
                '44':'сорок четыре градуса Цельсия','45':'сорок пять градусов Цельсия','46':'сорок шесть градусов Цельсия','47':'сорок семь градусов Цельсия','48':'сорок восемь градусов Цельсия','49':'сорок девять градусов Цельсия','50':'пятьдесят градусов Цельсия',
                '51':'пятьдесят один градус Цельсия','52':'пятьдесят два градуса Цельсия','53':'пятьдесят три градуса Цельсия','54':'пятьдесят четыре градуса Цельсия','55':'пятьдесят пять градусов Цельсия','56':'пятьдесят шесть градусов Цельсия','57':'пятьдесят семь градусов Цельсия',
                '58':'пятьдесят восемь градусов Цельсия','59':'пятьдесят девть градусов Цельсия','60':'шестьдесят градусов Цельсия'}

    response = requests.get(f'https://wttr.in/{sity}')

    forcast = response.text
    weat=forcast.find('°')
    #print(weat)
    #-- Отсчет для выделения значения температуры
    temp = forcast[weat-24:weat + 2]
    a=[k for k in temp[15::] ] #--Лист содержвщий температуру
    #b=[l for l in a[::-1] ] #--Обратный лист
    b=list(reversed(a))
    #print('Reversed:',b)
    temp_num=[]
    #print('Forward:',a)
    c=[tt for tt in b[7::]] #-- Укороченный лист
    #print('Filtered:',c)
    for qq in c:
        if qq == 'm':
            break
        else:
            temp_num.append(qq) #-- Добавление значений с температурой
            #print(q)
    #print(temp_num)
    d=[w for w in temp_num if not w == '\x1b'] # --  Исключение лишних знаков
    d=list(reversed(d))
    #print('Pure list',d)
    if len(d) == 3:
        temp_num_fin=[]
        temp_num_fin.append(d[1])
        temp_num_fin.append(d[2])
        temp_fin=''.join(temp_num_fin)
        #print(temp_fin)
        Temper_finaly=[]
        if d[0] == '-':
            Temper_finaly.append(Temper_s.get('-'))
            #print(Temper_finaly)
        for num in Temper_num.keys():
            if temp_fin == num:
                Temper_finaly.append(Temper_num.get(num))
                #print(Temper_num.get(num))
        #print(Temper_finaly)
        Temper_finaly_all=sity +':'+','.join(Temper_finaly)
        #print(Temper_finaly_all)
        return Temper_finaly_all

    elif len(d)==2:
        if d[0] == '-':
            temp_num_fin = []
            temp_num_fin.append(d[1])
            temp_fin=''.join(temp_num_fin)
            Temper_finaly=[]
            if d[0] == '-':
                Temper_finaly.append(Temper_s.get('-'))
            for num in Temper_num.keys():
                if temp_fin == num:
                    Temper_finaly.append(Temper_num.get(num))
            #print(Temper_finaly)
            Temper_finaly_all = sity + ':' + str(Temper_finaly)
            return Temper_finaly_all
        else:
            temp_num_fin = []
            temp_num_fin.append(d[0])
            temp_num_fin.append(d[1])
            temp_fin = ''.join(temp_num_fin)
            #print('Temperature:',temp_fin)
            Temper_finaly = []
            for num in Temper_num.keys():
                if temp_fin == num:
                    Temper_finaly.append(Temper_num.get(num))
                    print(Temper_num.get(num))
            #print(Temper_finaly)
            Temper_finaly_all=sity +':'+str(Temper_finaly)
            #print(Temper_finaly_all)
            return Temper_finaly_all

    elif len(d)==1:
        temp_num_fin = []
        temp_num_fin.append(d[0])
        temp_fin = ''.join(temp_num_fin)
        #print(type(temp_fin))
        #print(type(d))
        Temper_finaly = []
        #Temper_finaly = []
        for num in Temper_num.keys():
            if temp_fin == num:
                Temper_finaly.append(Temper_num.get(num))
                #print(Temper_num.get(num))
        #print(Temper_finaly)
        Temper_finaly_all = sity + ':' + str(Temper_finaly)
        #print(Temper_finaly_all)
        return Temper_finaly_all

#@functools.cache
def Temperature_sec():
    #time.sleep(2)
    #sity='Томск'
    Temper_sec={'-':'минус'}
    Temper_num_sec={'0':'ноль градусов Цельсия','1':'один градус Цельсия','2':'два градуса Цельсия','3':'три градуса Цельсия','4':'четыре градуса Цельсия','5':'пять градусов Цельсия','6':'шесть градусов Цельсия','7':'семь градусов Цельсия','8':'восемь градусов Цельсия','9':'девять градусов Цельсия',
                '10':'десять градусов Цельсия','11':'одиннадцать градусов Цельсия','12':'двенадцать градусов Цельсия','13':'тринадцать градусов Цельсия','14':'четырнадцать градусов Цельсия','15':'пятнадцать градусов Цельсия','16':'шестнадцать градусов Цельсия',
                '17':'семнадцать градусов Цельсия','18':'восемнадцать градусов Цельсия','19':'девятнадцать градусов Цельсия','20':'двадцать градусов Цельсия','21':'двадцать один градус Цельсия','22':'двадцать два градуса Цельсия','23':'двадцать три градуса Цельсия',
                '24':'двадцать четыре градуса Цельсия','25':'двадцать пять градусов Цельсия','26':'двадцать шесть градуса Цельсия','27':'двадцать семь градусов Цельсия','28':'двадцать восемь градусов Цельсия','29':'двадцать девять градусов Цельсия',
                '30':'тридцать градусов Цельсия','31':'тридцать один градус Цельсия','32':'тридцать два градуса Цельсия','33':'тридцать три градуса Цельсия','34':'тридцать четыре градуса Цельсия','35':'тридцать пять градусов Цельсия','36':'тридцать шесть градусов Цельсия',
                '37':'тридцать семь градусов Цельсия','38':'тридцать восемь градусов Цельсия','39':'тридцать девят градусов Цельсия','40':'сорок градусов Цельсия','41':'сорок один градус Цельсия','42':'сорок два градуса Цельсия','43':'сорок три градуса Цельсия',
                '44':'сорок четыре градуса Цельсия','45':'сорок пять градусов Цельсия','46':'сорок шесть градусов Цельсия','47':'сорок семь градусов Цельсия','48':'сорок восемь градусов Цельсия','49':'сорок девять градусов Цельсия','50':'пятьдесят градусов Цельсия',
                '51':'пятьдесят один градус Цельсия','52':'пятьдесят два градуса Цельсия','53':'пятьдесят три градуса Цельсия','54':'пятьдесят четыре градуса Цельсия','55':'пятьдесят пять градусов Цельсия','56':'пятьдесят шесть градусов Цельсия','57':'пятьдесят семь градусов Цельсия',
                '58':'пятьдесят восемь градусов Цельсия','59':'пятьдесят девть градусов Цельсия','60':'шестьдесят градусов Цельсия'}
    
    
    url=requests.get('https://api.open-meteo.com/v1/forecast?latitude=55.0415&longitude=82.9346&current_weather=true&windspeed_unit=ms&timezone=auto')
    tempr=url.text
    #print(json.loads(temp))
    temp_js=json.loads(tempr)
    temp_di=temp_js.setdefault('current_weather')
    temp_val=temp_di.setdefault('temperature')
    temp_wind=temp_di.setdefault('windspeed')
    #print('Meteo:',temp_di)
    print('Meteo:',temp_val,'C')
    #print('Meteo:',temp_wind,'м/с')
    #print(temp_val)
    temp_spl=str(temp_val)
    #print(len(temp_spl))
    # Если температура формата -хх.х
    #speek('По данным другого источника')
    if len(temp_spl) == 5:
        Temper_fin_sec=[]
        if temp_spl[0] == '-':
            Temper_fin_sec.append(Temper_sec.get('-'))
        for num_sec in Temper_num_sec.keys():
            if temp_spl[1:3] == num_sec:
                Temper_fin_sec.append(Temper_num_sec.get(num_sec))
        print(Temper_fin_sec)
        return ','.join(Temper_fin_sec)
    #Если температура формата -х.х или xx.x
    elif len(temp_spl) == 4:
        if temp_spl[0] != '-':  # Формат хх.х
            Temper_fin_sec=[]
            for num_sec in Temper_num_sec.keys():
                if temp_spl[0:2] == num_sec:
                    Temper_fin_sec.append(Temper_num_sec.get(num_sec))
            print(Temper_fin_sec)
            return ','.join(Temper_fin_sec)
        else: #Формат -х.х
            Temper_fin_sec=[]
        if temp_spl[0] == '-':
            Temper_fin_sec.append(Temper_sec.get('-'))
        for num_sec in Temper_num_sec.keys():
            if temp_spl[1] == num_sec:
                Temper_fin_sec.append(Temper_num_sec.get(num_sec))
        print(Temper_fin_sec)
        return ','.join(Temper_fin_sec)

    #Если температура формата х.х
    elif len(temp_spl) == 3:
        Temper_fin_sec=[]
        for num_sec in Temper_num_sec.keys():
            if temp_spl[0] == num_sec:
                Temper_fin_sec.append(Temper_num_sec.get(num_sec))
        print(Temper_fin_sec)
        return ','.join(Temper_fin_sec)


def wind():
    time.sleep(5)#3
    Wind={'1':' один метр в секунду','2':'два метра в секунду','3':'три метра в секунду','4':'четыре метра в секунду','5':'пять метров в секунду','6':'шесть метров в секунду','7':'семь метров в секунду','8':'восемь метров в секунду','9':'девять метров в секунду',
                '10':'десять метров в секунду','11':'одиннадцать метров в секунду','12':'двенадцать метров в секунду','13':'тринадцать метров в секунду','14':'четырнадцать метров в секунду','15':'пятнадцать метров в секунду','16':'шестнадцать метров в секунду',
                '17':'семнадцать метров в секунду','18':'восемнадцать метров в секунду','19':'девятнадцать метров в секунду','20':'двадцать метров в секунду','21':'двадцать один метр в секунду','22':'двадцать два метра в секунду','23':'двадцать три метра в секунду',
                '24':'двадцать четыре метра в секунду','25':'двадцать пять метров в секунду','26':'двадцать шесть градуса Цельсия','27':'двадцать семь градусов Цельсия','28':'двадцать восемь градусов Цельсия','29':'двадцать девять градусов Цельсия',
                '30':'тридцать градусов Цельсия','31':'тридцать один градус Цельсия','32':'тридцать два градуса Цельсия','33':'тридцать три градуса Цельсия','34':'тридцать четыре градуса Цельсия','35':'тридцать пять градусов Цельсия','36':'тридцать шесть градусов Цельсия',
                '37':'тридцать семь градусов Цельсия','38':'тридцать восемь градусов Цельсия','39':'тридцать девят градусов Цельсия','40':'сорок градусов Цельсия','41':'сорок один градус Цельсия','42':'сорок два градуса Цельсия','43':'сорок три градуса Цельсия',
                '44':'сорок четыре градуса Цельсия','45':'сорок пять градусов Цельсия','46':'сорок шесть градусов Цельсия','47':'сорок семь градусов Цельсия','48':'сорок восемь градусов Цельсия','49':'сорок девять градусов Цельсия','50':'пятьдесят градусов Цельсия',
                '51':'пятьдесят один градус Цельсия','52':'пятьдесят два градуса Цельсия','53':'пятьдесят три градуса Цельсия','54':'пятьдесят четыре градуса Цельсия','55':'пятьдесят пять градусов Цельсия','56':'пятьдесят шесть градусов Цельсия','57':'пятьдесят семь градусов Цельсия',
                '58':'пятьдесят восемь градусов Цельсия','59':'пятьдесят девть градусов Цельсия','60':'шестьдесят градусов Цельсия'}
    url_wind=requests.get('https://api.open-meteo.com/v1/forecast?latitude=56.47&longitude=84.98&current_weather=true&windspeed_unit=ms&timezone=auto')
    wind_sec=url_wind.text
    #print(json.loads(wind_sec))
    wind_js=json.loads(wind_sec)
    wind_di=wind_js.setdefault('current_weather')
    temp_wind=wind_di.setdefault('windspeed')
    wind_str=str(temp_wind)
    print(temp_wind)
    #print(wind_str[0],len(wind_str))
    if temp_wind < 1:
        print('штиль')
        return 'ветер, штиль'
    elif len(wind_str)==4:
        wind_add=[]
        for w in Wind.keys():
            if wind_str[0] == w:
                wind_add.append(Wind.get(w))
        print(wind_add)
        return 'ветер,'+','.join(wind_add)
    elif len(wind_str) == 5:
        wind_add=[]
        for w in Wind.keys():
            if wind_str[0:2] == w:
                wind_add.append(Wind.get(w))
        print(wind_add)
        return 'ветер,'+','.join(wind_add)
    elif len(wind_str)==3:
        wind_add=[]
        for w in Wind.keys():
            if wind_str[0] == w:
                wind_add.append(Wind.get(w))
        print(wind_add)
        return 'ветер,'+','.join(wind_add)




'''
def speek(text):
    language = 'ru'
    model_id = 'ru_v3'
    sample_rate = 48000
    speaker = 'xenia'
    put_accent = True
    put_yo = True
    device = torch.device('cpu')
    torch.set_num_threads(4)
    #text = 'девятнадцать часов, тридцать минут'
    model, _ =torch.hub.load(repo_or_dir='snakers4/silero-models',
                            model='silero_tts',
                            language=language,
                            speaker=model_id)
    model.to(device)

    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    print(text)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate)
    sd.stop()
'''
import pyttsx3
#def second_speak(text):
def speek(text):
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', 'ru')


    for voice in voices:
        if voice.name == 'Aleksandr':
            tts.setProperty('voice', voice.id)

    #tts.say('Командный голос вырабатываю, товарищ генерал-полковник!')
    tts.say(text)
    tts.runAndWait()
    tts.stop()

#speek(Temperature_sec())
#speek(Time_to())
#Temperature()
#Temperature_sec()
#wind()

