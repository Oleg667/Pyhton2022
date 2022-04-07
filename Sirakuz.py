# x=int(input('Введите число -> '))
# n=1
# y=x
# while x!=1:
#     if x%2==0:
#         x=x/2
#         n=n+1
#         print(x)
#     else:
#         x=x*3+1
#         i=x
#         n=n+1
#         print(x)
# print(f'число {y} привелось к 1 за {n} циклов')
n = 9
for i in range(n):
    print(''.join(map(str, range(1, i+2))))
