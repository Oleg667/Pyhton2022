# Гришаев Олег группа Q73.

def sort(array):#функция сортировки
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):
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
        array = input('Введите, пожалуйста, через пробел некоторые целые числа от 0 до 100: ').split()
        array_list = list(map(int, array))
        array_sort = sort(array_list)
        for i in array_sort:
            if i < 0 or i > 100:
                raise Exception
        break
    except ValueError:
        print('Введите целые числа, через пробел, от 0 да 100.')  # проверка если ввели не число
        exit()
    except Exception:
        print('Введите числа не меньше 0 и не больше 100.') # проверка на попадание чисел в интервал от 9 до 100
        exit()

while True:
    try:
        numeral = int(input('Введите, пожалуйста, искомое число: '))
        array_sort.append(numeral)
        array_sort = sort(array_sort)
        if numeral < 0 or numeral > 100:
            raise Exception
        break
    except ValueError:
        print('Введите, пожалуйста, ЦЕЛОЕ ЧИСЛО.')  # Отслеживается ошибка значений - число с запятой..
        exit()
    except Exception:
        print('Введите число не меньше 0 и не больше 100.')
        exit()

print(f'Отсортированный числовой массив: {array_sort}.')

numeral_in = binary_search(array_sort, numeral, 0, len(array_sort))
small_in = numeral_in - 1
big_in = numeral_in + 1

print(f'Индекс вашего числа в массиве: {numeral_in}.')

if small_in in range(len(array_sort)):
    print(f'Индекс предыдущего меньшего числа: {small_in}.')
else:
    print(f'Индекс предыдущего меньшего числа: {small_in}, вне (меньше) диапазона.')

if big_in in range(len(array_sort)):
    print(f'Индекс следующего большего числа: {big_in}.')
else:
    print(f'Индекс предыдущего большего числа: {big_in}, вне (больше) диапазона.')

if array_sort[numeral_in] == array_sort[big_in]:
    print('Ваше число равно следующему числу.')
else:
    ...