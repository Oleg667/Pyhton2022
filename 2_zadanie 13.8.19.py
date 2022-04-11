#задание 13.8.19
# запрвшивает количество билетов, проверяет на корректрность ввода.
# в случае ошибки ввода предлагает повторить ввод или закончить работу
# вариант первый предусматривал ввод возрастной группы по каждому билету (он проще),
# но если билетов большОе количество, то это превращается в длительный процесс.
# по этому программа запрашивает количество билетов возрастной группы,
# в случае если введенное количество больше остатка нераспределенных билетов то
# считается что все оставшиеся билеты для данной возрастной группы.


def vvod_int(voz,ost): # функция запроса количества ввода посетителей определенного возраста, с индикацией остатка билетов
    while True:
        try:
            kol = abs(int(input(f'Введите количество посетителей {voz} осталось {ost} бил. > ')))
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
vozrast2=0 # количество посетителей от 18 до 25
vozrast3=0 # количество посетителей старше 25
# вспомогательные переменные
v1 = 0
v2 = 0
v3 = 0


i=1
while kol_biletov > raspred:
    # while True:
        vozrast1 = vvod_int("моложе 18",kol_biletov-raspred)

        if  vozrast1 >= (kol_biletov-raspred):
            vozrast1=v1 + (kol_biletov-raspred)
            break
        else:
            raspred = raspred + vozrast1
            vozrast1 = vozrast1 + v1
            vozrast2 = vvod_int("от 18 до 25", kol_biletov-raspred)
            if vozrast2 >= (kol_biletov-raspred):
                vozrast2=v2+(kol_biletov-raspred)
                break
            else:
                raspred = raspred + vozrast2
                vozrast2 = vozrast1 + v2
                vozrast3 = vvod_int("старше 25", kol_biletov-raspred)
                if vozrast3 >= (kol_biletov - raspred):
                    vozrast3 = v3+(kol_biletov - raspred)
                    break
                else:
                    raspred = raspred + vozrast3
                    print(f'не распределено {kol_biletov-raspred} билетов')
                    v1 = vozrast1
                    v2 = vozrast2
                    v3 = vozrast3

print(f'Бесплатных билетов - {vozrast1} шт')
print(f'Билетов по 990 руб. - {vozrast2} шт')
print(f'Билетов по 1390 руб. - {vozrast3} шт')

# блок расчета итоговой суммы
summa=(vozrast2*990+vozrast3*1390)
if kol_biletov>3:
    summa=float(summa)*0.9
    print(f'Итого к оплате за {kol_biletov} бил., с учетом скидки 10%: {summa}')
else:
    print(f'Итого к оплате за {kol_biletov} бил. : {summa}')
