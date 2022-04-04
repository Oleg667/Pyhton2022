# ввод суммы
mony=int(input('введите количество денег  >'))

# банки и ставки
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

#список банков
banks = list(per_cent.keys())

# блок вычислений, округление до второго знака после запятой (до копеек)

tkb=round(((per_cent.get('ТКБ'))*mony/100),2)
skb=round((per_cent.get('СКБ'))*mony/100,2)
vtb=round((per_cent.get('ВТБ'))*mony/100,2)
sber=round((per_cent.get('СБЕР'))*mony/100,2)

deposit = [tkb,skb,vtb,sber]
print ('\n' , list(map(int, deposit))) # формат int что бы совпадало с примером в блоке, как вариант можно округлить до целого.

print('\n', deposit) # фактические значения

#вывод дохода по всем банкам
print(f'\nДоход по депозиту составит:\n{banks[0]} банк - {deposit[0]} рублей\n{banks[1]} банк - {deposit[1]} '
      f'рублей\n{banks[2]} банк - {deposit[2]} рублей\n{banks[3]} банк - {deposit[3]} рублей\n')

#вывод максимальной суммы
print('Максимальная сумма, которую вы можете заработать — '+ str(max(deposit)) +' рублей')


