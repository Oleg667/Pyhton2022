
# global x # объявляем, что переменная является глобальной
x = 3
def func():
   global x
   print(x)
   x = 5
   x += 5
   return
def func1():
   #global x
   print(x)
   x = 5
   x += 5
   return


func()
func1()
print(x)