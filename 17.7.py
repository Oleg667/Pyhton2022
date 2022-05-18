# #на вход программы поступает массив из произвольного количества целых чисел и
# # ещё одно целое число, которое будем проверять на вхождение в этот массив.
# # Задача состоит в том, чтобы вернуть индекс первого вхождения элемента,
# # если он входит в него, и False если не входит.
# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))
#****************************
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# n = 0
# y=0
# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     print('i= ',i)
#     y=y+1
#     for j in range(i, len(array)):
#         if array[j] < array[idx_min]:
#             n=n+1
#             print(n)
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#        #n=n+1
#        array[i], array[idx_min] = array[idx_min], array[i]
#
# print(array)
# print(n,y)
#******************************
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
n = 0
y=0
for i in range(1, len(array)):
    x = array[i]
    idx = i

    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        y=y+1
    array[idx] = x
print(array)
print(n,y)