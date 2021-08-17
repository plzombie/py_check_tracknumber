# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:24:34 2021

@author: misha
"""

def mail_info(sign):
    if sign[0] == 'R':
        return 'Регистрируемое отправление (до 2 кг)'
    elif sign[0] == 'L':
        return 'Отслеживоемое письмо'
    elif sign[0] == 'V':
        return 'Письмо с объявленной ценностью'
    elif sign[0] == 'C':
        return 'Международная посылка (более 2 кг)'
    elif sign[0] == 'E':
        return 'Экспресс отправление (EMS)'
    elif sign[0] == 'U':
        return 'Нерегистрируемое и неотслеживаемое отправление'
    elif sign[0] == 'Z':
        return 'Простой регистрируемый пакет (SRM)'
    else:
        return sign


def country_info(iso):
    if iso == 'AE':
        return 'ОАЭ'
    elif iso == 'AM':
        return 'Армения'
    elif iso == 'AR':
        return 'Аргентина'
    elif iso == 'AT':
        return 'Австрия'
    elif iso == 'AU':
        return 'Австралия'
    elif iso == 'AZ':
        return 'Азербайджан'
    elif iso == 'BG':
        return 'Болгария'
    elif iso == 'BR':
        return 'Бразилия'
    elif iso == 'BY':
        return 'Белоруссия'
    elif iso == 'CA':
        return 'Канада'
    elif iso == 'CH':
        return 'Швейцария'
    elif iso == 'CN':
        return 'Китай'
    elif iso == 'CU':
        return 'Куба'
    elif iso == 'CZ':
        return 'Чехия'
    elif iso == 'DE':
        return 'Германия'
    elif iso == 'DK':
        return 'Дания'
    elif iso == 'EE':
        return 'Эстония'
    elif iso == 'EG':
        return 'Египет'
    elif iso == 'ES':
        return 'Испания'
    elif iso == 'FI':
        return 'Финляндия'
    elif iso == 'FR':
        return 'Франция'
    elif iso == 'GB':
        return 'Великобритания'
    elif iso == 'GE':
        return 'Грузия'
    elif iso == 'GR':
        return 'Греция'
    elif iso == 'GL':
        return 'Гренландия'
    elif iso == 'HK':
        return 'Гонконг'
    elif iso == 'HU':
        return 'Венгрия'
    elif iso == 'IE':
        return 'Ирландия'
    elif iso == 'IL':
        return 'Израиль'
    elif iso == 'IN':
        return 'Индия'
    elif iso == 'IR':
        return 'Иран'
    elif iso == 'IS':
        return 'Исландия'
    elif iso == 'IT':
        return 'Италия'
    elif iso == 'JP':
        return 'Япония'
    elif iso == 'KG':
        return 'Киргизия'
    elif iso == 'KP':
        return 'Северная Корея'
    elif iso == 'KR':
        return 'Южная Корея'
    elif iso == 'KZ':
        return 'Казахстан'
    elif iso == 'LT':
        return 'Литва'
    elif iso == 'LV':
        return 'Латвия'
    elif iso == 'MC':
        return 'Монако'
    elif iso == 'MD':
        return 'Молдавия'
    elif iso == 'MN':
        return 'Монголия'
    elif iso == 'MX':
        return 'Мексика'
    elif iso == 'NO':
        return 'Норвегия'
    elif iso == 'NZ':
        return 'Новая Зеландия'
    elif iso == 'PH':
        return 'Филиппины'
    elif iso == 'PL':
        return 'Польша'
    elif iso == 'PT':
        return 'Португалия'
    elif iso == 'RO':
        return 'Румыния'
    elif iso == 'RS':
        return 'Сербия'
    elif iso == 'RU':
        return 'Россия'
    elif iso == 'SA':
        return 'Саудовская Аравия'
    elif iso == 'SE':
        return 'Швеция'
    elif iso == 'SG':
        return 'Сингапур'
    elif iso == 'SI':
        return 'Словения'
    elif iso == 'SK':
        return 'Словакия'
    elif iso == 'TJ':
        return 'Таджикистан'
    elif iso == 'TM':
        return 'Туркмения'
    elif iso == 'TR':
        return 'Турция'
    elif iso == 'TW':
        return 'Тайвань'
    elif iso == 'UA':
        return 'Украина'
    elif iso == 'US':
        return 'США'
    elif iso == 'VE':
        return 'Венесуэла'
    elif iso == 'VN':
        return 'Вьетнам'
    elif iso == 'UZ':
        return 'Узбекистан'
    return iso

def is_num(text):
    for t in text:
        if t.isdigit() == False:
            return False
    return True


def check_checksum_ww(tracknum):
    control = int(tracknum[10])-int('0')
    num1 = int(tracknum[2])-int('0')
    num2 = int(tracknum[3])-int('0')
    num3 = int(tracknum[4])-int('0')
    num4 = int(tracknum[5])-int('0')
    num5 = int(tracknum[6])-int('0')
    num6 = int(tracknum[7])-int('0')
    num7 = int(tracknum[8])-int('0')
    num8 = int(tracknum[9])-int('0')
    
    calc_control = 11-(num1*8+num2*6+num3*4+num4*2+num5*3+num6*5+num7*9+num8*7)%11
    if calc_control == 10:
        calc_control = 0
    elif calc_control == 11:
        calc_control = 5
        
    if calc_control == control:
        return True
    else:
        return False


def check_checksum_ru(tracknum):
    control = int(tracknum[13])-int('0')
    sum1 = 0
    sum2 = 0
    for i in range(0,14,2):
        sum1 += (int(tracknum[i])-int('0'))
    sum1 *= 3
    for i in range(1,13,2):
        sum2 += int(tracknum[i])-int('0')
    calc_control = 10-(sum1+sum2)%10
    if control == calc_control:
        return True
    else:
        return False
    

def main():
    tracknum = input("Введите трек-номер: ")
    
    if len(tracknum) == 13 and is_num(tracknum) == False:
        sign = tracknum[:2]
        iso = tracknum[11:]
        
        print(mail_info(sign))
        print("Место отправления", country_info(iso))
        if(check_checksum_ww(tracknum) == True):
            print("Трек номер корректный")
            print("Используйте ссылку","https://www.pochta.ru/tracking#" + tracknum, "для отслеживания посылки")
        else:
            print("Неправильный трек номер (контрольная сумма не совпадает)")
    elif len(tracknum) == 13 and is_num(tracknum) == True:
        print('Внутренний трек-номер')
    elif len(tracknum) == 14:
        print('Индекс отправителя:', tracknum[:6])
        if(check_checksum_ru(tracknum) == True):
            print("Трек номер корректный")
            print("Используйте ссылку","https://www.pochta.ru/tracking#" + tracknum, "для отслеживания посылки")
        else:
            print("Неправильный трек номер (контрольная сумма не совпадает)")


main()
