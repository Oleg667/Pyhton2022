# Гришаев  Олег группа Q73.

def sort(array):#функция сортировки
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right): #поиск номера позиции элемента
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


while True:
    try:
        array = input('Введите через пробел некоторые целые числа от 0 до 100 > ').split()
        array_list = list(map(int, array))

        for i in array_list:
            if i < 0 or i > 100:
                raise Exception
        break
    except ValueError:
        print('Ошибка, вводить надо только целые числа от 0 да 100.')  # проверка если ввели не число
        exit()
    except Exception:
        print('Ошибка число не в интервале от 0 до 100.') # проверка на попадание чисел в интервал от 9 до 100
        exit()

while True:
    try:
        numeral = int(input('Введитите целое число от 0 до 100 > '))

        array_list.append(numeral) #добавляем введенное число в список
        array_sort = sort(array_list)

        if numeral < 0 or numeral > 100:
            raise Exception
        break
    except ValueError:# проверка что введено целое число
        print('Ошибка! это не целое число.')
        exit()
    except Exception: # проверка что число в заданном интервале
        print('Ошибка! число не в интервале от 0 до 100.')
        exit()


numeral_in = int(binary_search(array_sort, numeral, 0, len(array_sort)))

if numeral <= array_sort[0]:
    print('Все числа из последовательности больше заданного числа')

elif numeral >= array_sort[-1]:
    print('Все числа из последовательности меньше или равны заданному числу')

else:
    print(f'\nномер позиции элемента, который меньше введенного числа,\n а следующий за ним больше или равен этому числу.:', (numeral_in-1))

