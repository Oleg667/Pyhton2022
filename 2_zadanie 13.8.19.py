#задание 13.8.19
def vvod_int(voz,ost): # функция запроса количества ввода посетителей определенного возраста, с проверкой остатка билетов
    while True:
        try:
            kol = int(input(f'Введите количество посетителей {voz} осталось {ost} бил. > '))
            # return kol
            #break
        except ValueError:
            print('введено некорректное значение, введите целое положительное число')
            stop = input('если хотите продолжить введите Да иначе Нет >')
            print(stop)
            if stop == 'Нет':
                exit()
        return kol






# ввод количества билетов с проверкой что ввели целое положительное число
while True:
    try:
        kol_biletov=int(input('Введите количество билетов которое хотите приобрести? > '))
        break
    except ValueError:
        print( 'введено некорректное значение, введите целое положительное число')
        stop=input('если хотите продолжить введите Да иначе Нет >')
        print(stop)
        if stop=='Нет':
            exit()

# блок ввода количества посетителей определенного возраста

summa=0  #сумма которую нужно заплатить за билеты
raspred=0 # количество расспределенных билетов
vozrast1=0 # количество посетителей моложе 18 лет
vozrast2=0 # количество поситителей от 18 до 25
vozrast3=0 # количество поситителей старше 25
i=1
while kol_biletov > raspred:  # если билетов много, то вводить данные по каждому очень долго
    # while True:
        vozrast1 = vvod_int("моложе 18",kol_biletov)

        if  vozrast1 >= kol_biletov:
            vozrast1=kol_biletov
            break
        else:
            raspred=raspred+vozrast1
            vozrast2 = vvod_int("от 18 до 25", raspred)
            print(raspred)
            if vozrast2 >= (kol_biletov-raspred):
                vozrast2=(kol_biletov-raspred)
                break
            else:
                raspred = raspred + vozrast2
                vozrast2 = (kol_biletov - raspred)
                vozrast3 = vvod_int("старше 25", raspred)
                if vozrast3 >= (kol_biletov - raspred):
                    vozrast3 = (kol_biletov - raspred)
                    break
                else:
                    raspred = raspred + vozrast3
                    vozrast3 = (kol_biletov - raspred)
                    print(f'не распределено {kol_biletov-raspred} билетов')



# блок расчета итоговой суммы
if kol_biletov>3:
    summa=float(summa)*0.9
    print(f'Итого к оплате за {kol_biletov} бил., с учетом скидки 10%: {summa}')
else:
    print(f'Итого к оплате за {kol_biletov} бил. : {summa}')
kol_biletov=int(1)
c=type(kol_biletov)
print(c)