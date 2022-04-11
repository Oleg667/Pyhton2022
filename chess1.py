# a1 = input('первая клетка координата 1')
# a2 = input('первая клетка координата 2')
# b1 = input('вторая клетка координата 1')
# b2 = input('вторая клетка координата 2')
# xy1=['1','3','5','7']
# xy2=['2','4','6','8']
# if a1 in xy1 and a2 in xy1:
#   pr1="черная"
#   print(pr1)
# elif a1 in xy2 and a2 in xy2:
#     pr1 = "черная"
#     print(pr1)
# else:
#     pr1 = "белая"
#     print (pr1)
# if b1 in xy1 and b2 in xy1:
#   pr2="черная"
#   print(pr2)
# elif b1 in xy2 and b2 in xy2:
#     pr2 = "черная"
#     print(pr2)
# else:
#     pr2 = "белая"
#     print (pr2)
# if pr1==pr2:
#     print(1)
# Мое решение
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if (b1==a1+1 and b2==a2-1) or (b1==a1+1 and b2==a2) or (b1==a1+1 and b2==a2+1)\
(b1==(a1) and b2==(a2-1)) or (b1==(a1) and b2==(a2+1))\
(b1==(a1-1) and b2==(a2-1)) or (b1==(a1-1) and b2==(a2))or(b1==(a1-1) and b2==(a2+1)):
    print('YES')
else:
    print('NO')