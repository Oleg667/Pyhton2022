from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()
#print(Fore.BLACK)
#print(Back.GREEN)

what = input("Что делаем?(+,-,*):")
print(what)

#if what=="+":
#elif what =="-":
#elif what=="*":
#print(Back.CYAN)
    # a = float(input("Введи первое число:"))
    # b = float(input("Введи второе число:"))
    # print(Back.YELLOW)
# c = 0
if what == "+":
        a = float(input("Введи первое число:"))
        b = float(input("Введи второе число:"))
        c = a + b
elif what == "-":
        a = float(input("Введи первое число:"))
        b = float(input("Введи второе число:"))

        c = a - b
elif what == "*":
        a = float(input("Введи первое число:"))
        b = float(input("Введи второе число:"))
        c = a * b
else:
        c = "Неправильный выбор!"

print("Результат:" + str(c))

input()