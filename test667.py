#print (120 % 70)
#print (-120 % 50)
# f = 653457
# g = 123493
# print(f**g)
# a=1.3
# print(a)
# b=2.3
# print(b)
# c=a+b
# print(c)
# print(a+b)
# print(1.3+2.3)
# print(24/4)
# print(2.4/0.4)
# print(round((11*2.5/3),2))
# print(round(3.14159**2/2,0))
# print (divmod(10, 3))
# print (divmod(10,-3))
# stroka=input('enter the numbers separated by a space')
# stroka1=stroka.split()
# stroka3='\n'.join(stroka1)
# print(stroka3)
#pi = 31.4159265
#print ("%.4e" % (pi))
# day = 14
# month = 2
# year = 2012
#
# print("%d.%02d.%d" % (day, month, year))
# # 14.02.2012
# print("%d-%02d-%d" % (year, month, day))
# # 2012-02-14
# print("%d/%d/%d" % (year, day, month))
# # 2012/14/2
# hours=11
# minutes=2
# seconds=14
# cake = ('c','a','k','e')
# print(type(cake))
#
#
# print("%02d:%02d:%d" % (hours, minutes, seconds))
# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# print(string)
#
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
# a=sum(list_of_numbers[::])
#
# pos=len(list_of_numbers)
# print('в строке значений =',pos)
# pos1=pos-1
# print(list_of_numbers[pos1])
# print(string)
# print((list_of_numbers[::3]))
# x=(sum(list_of_numbers[::])) # sum() вычисляет сумму элементов списка
# x=float(x)
# print(x)
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))

title=input("введите название книги")
name=input("введите имя автора")
year=int(input("введите год издания"))
dict={'title':title,'name':name,'ear':year}
print (dict)