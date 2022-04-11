#задание 13.8.19

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

summa=0  #сумма которую нужно заплатить за билеты

i=1
while i<=kol_biletov:
    vozrast=int(input(f'введите возраст посетителя для {i}го билета  > '))
    if vozrast <18:
        summa=summa
    elif vozrast<25:
        summa=summa+990
    else:
        summa = summa + 1390
    i=i+1
if kol_biletov>3:
    summa=float(summa)*0.9
    print(f'Итого к оплате за {kol_biletov} бил., с учетом скидки 10%: {summa}')
else:
    print(f'Итого к оплате за {kol_biletov} бил. : {summa}')
kol_biletov=int(1)
c=type(kol_biletov)
print(c)