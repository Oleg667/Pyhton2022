#задание 13.8.19
def vvod_int(voz,ost): # функция запроса количества ввода посетителей определенного возраста, с проверкой остатка билетов
    while True:
        try:
            kol = int(input(f'Введите количество поситителей {voz} > '))
            break
        except ValueError:
            print('введено некорректное значение, введите целое положительное число')
            stop = input('если хотите продолжить введите Да иначе Нет >')
            print(stop)
            if stop == 'Нет':
                exit()
return: kol






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
ostatok=0
vozrast1=0
vozrast2=0
vozrast3=0
i=1
while (kol_biletov - ostatok) > 0:  # если билетов много, то вводить данные по каждому очень долго
    vozrast1 = int(input(f'Введите количество поситителей младше 18 лет из {kol_biletov-ostatok} > '))
    if ostatok <= kol_biletov:
      ostatok = ostatok+vozrast1
    else:           #если введено число больше чем всего билетов то количество моложе 18 лет равно количеству билетов
        ostatok=kol_biletov
        vozrast1=ostatok
        if ostatok < kol_biletov:
            vozrast2 = int(input(f'Введите количество поситителей старше 18 но младше 25 лет из {kol_biletov-ostatok} > '))
            if (ostatok+vozrast2) <= kol_biletov:
                ostatok = ostatok + vozrast1
            else:  # если введено число больше чем оставшихся билетов то количество от 18 до 25 лет равно количеству оставшихся билетов билетов
                vozrast2 = kol_biletov - ostatok
                ostatok = kol_biletov
        else:

            if ostatok < kol_biletov:
                vozrast3 = int(input(f'Введите количество поситителей старше 25 лет {kol_biletov-ostatok} > '))

if kol_biletov>3:
    summa=float(summa)*0.9
    print(f'Итого к оплате за {kol_biletov} бил., с учетом скидки 10%: {summa}')
else:
    print(f'Итого к оплате за {kol_biletov} бил. : {summa}')
kol_biletov=int(1)
c=type(kol_biletov)
print(c)