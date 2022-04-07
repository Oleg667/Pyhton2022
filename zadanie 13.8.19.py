# задание 13.8.19
kol_biletov=int(input('Введите количество билетов которое хотите приобрести? > '))

summa=0  # сумма которую нужно заплатить за билеты

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
