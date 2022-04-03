mony=int(input('введите количество денег  >'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb=(per_cent.get('ТКБ'))*mony/100
skb=(per_cent.get('СКБ'))*mony/100
vtb=(per_cent.get('ВТБ'))*mony/100
sber=(per_cent.get('СБЕР'))*mony/100

deposit = [tkb,skb,vtb,sber]
# #max_deposit=max(deposit)


deposit = [tkb,skb,vtb,sber]

print (list(map(int, deposit)))
print('Максимальная сумма, которую вы можете заработать — '+str(max(deposit)))


