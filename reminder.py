import datetime
import os.path
import time
import os


def reminder(tme, dte, what):
    a = []  #Список сущ. файлов
    for i in range (1, 5):# проверка на существование файла, если есть, то +1
        if os.path.exists(f'rem_{i}.txt') == True:
            a.append(i)
            i=i+1
    print(a)

    with open(f'rem_{(len(a)+1)}.txt', 'a') as f: #длина списка а+1 для имени
        for j in tme, dte, what:
            f.write(f'{j}\n') #f.write(f'{j} \n')
        #f.write(str(tme))
    #Проверка на отсутствие файла в середине списка
    for i in range(1,len(a)+1):
        if i in a:
            pass
        else:
            print(i)
            with open(f'rem_{i}.txt', 'a') as f:
                for j in tme ,dte, what:
                    f.write(j)
#Читает каждый файл.

def reminder_check():
    a = []  # Список сущ. файлов
    for i in range(1, 5):  # проверка на существование файла, если есть, то +1
        if os.path.exists(f'rem_{i}.txt') == True:
            a.append(i)
            i = i + 1
        if a == []:
            print('Not exist')
            exit()
    dt = datetime.datetime.now()
    #print(datetime.datetime.now().date())
    #print(dt.strftime('%H:%M'),'now')
    while True:
        for i in range(1,(len(a)+1) ):
            with open(f'rem_{i}.txt', 'r') as f:
                file = f.readlines()
                #print(file)
                #время в строку
                pure_tme = file[0].split()
                pure_tme_next = (''.join(pure_tme))
                #print(pure_tme)
                if '-' in pure_tme_next:
                    pure_tme_next = pure_tme_next.replace('-',':')
                #print(pure_tme_next)
                #print(new_time)
                #дату в строку
                dte = file[1].split()
                dte_str = ''.join(dte)
                #print(dte_str)
                #print(len(dte_str)
                #Разбиение по дате
                if len(dte_str) == 5:
                    day = dte_str[0] + dte_str[1]
                    #print('Day:', day)
                    month = dte_str[3] + dte_str[4]
                    #print('Month', month)
                    full_dte = '2023-' + month + '-' + day  # поменять год на динамику
                    # print(full_dte)
                    # print(full_dte == str(datetime.datetime.now().date())) #Совпадает ли дата из файла и дата по текущему времени
                    if pure_tme_next in str(datetime.datetime.now().time()) and full_dte == str(
                            datetime.datetime.now().date()):
                        #print(file[2])
                        return file[2]
                        f.close()
                        os.remove(f'rem_{i}.txt')
                    else:
                        pass
                if len(dte_str) == 4:
                    day = dte_str[0]+dte_str[1]
                    #print('Day:',day)
                    month = dte_str[2]+dte_str[3]
                    #print('Month',month)
                    full_dte = '2023-' + month + '-' + day  #поменять год на динамику
                    #print(full_dte)
                    #print(full_dte == str(datetime.datetime.now().date())) #Совпадает ли дата из файла и дата по текущему времени
                    if pure_tme_next in str(datetime.datetime.now().time()) and full_dte == str(datetime.datetime.now().date()):
                        print(file[2])
                        return  file[2]
                        f.close()
                        os.remove(f'rem_{i}.txt')
                    else:
                        pass

                    #print()
                if len(dte_str) == 3:
                    day = dte_str[0]
                    #print('Day:',day)
                    month = dte_str[1]+dte_str[2]
                    #print('Month',month)
                    full_dte = '2023-' + month + '-' + day  # поменять год на динамику
                    #print(full_dte in str(datetime.datetime.now().date()))
                    if pure_tme_next in str(datetime.datetime.now().time()) and full_dte == str(datetime.datetime.now().date()):
                        print(file[2])
                        return file[2]
                        f.close()
                        os.remove(f'rem_{i}.txt')
                    else:
                        pass
                    #print('__________________________________________________')

                #if pure_tme_next in str(datetime.datetime.now().time()) :
                    #print('ok')
                    #print(file[2])
        time.sleep(20)


#reminder(str(datetime.datetime.now()), str(datetime.date.today()), 'test')
#reminder_check()

