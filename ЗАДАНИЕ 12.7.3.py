mony=int(input('введите количество денег  >'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
banks = list(per_cent.keys())
tkb=(per_cent.get('ТКБ'))*mony/100
skb=(per_cent.get('СКБ'))*mony/100
vtb=(per_cent.get('ВТБ'))*mony/100
sber=(per_cent.get('СБЕР'))*mony/100

deposit = [tkb,skb,vtb,sber]
print (list(map(int, deposit)))


print(f'\nДоход по депозиту составит:\n{banks[0]} банк - {deposit[0]} рублей\n{banks[1]} банк - {deposit[1]} '
      f'рублей\n{banks[2]} банк - {deposit[2]} рублей\n{banks[3]} банк - {deposit[3]} рублей\n')

print('Максимальная сумма, которую вы можете заработать — '+str(max(deposit))+' рублей')
max_deposit=max(deposit)
print('Максимальная сумма, которую Вы можете заработать: {} рублей.'.format(max_deposit))


