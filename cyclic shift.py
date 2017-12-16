# -*-coding:UTF-8-*-


def cyclic_shift_left(a):  # Циклический сдвиг влево
    """
    Циклический сдвиг
    :param a: Массив
    :return: Массив со сдвинутыми значениями
    """
    tmp = a[0]
    for i in range(len(a)-1):
        a[i] = a[i+1]
    a[len(a) - 1] = tmp
    return a


def cyclic_shift_right(a):  # Циклический сдвиг вправо
    tmp = a[len(a) - 1]
    for i in range(len(a) - 2, -1, -1):
        a[i+1] = a[i]
    a[0] = tmp
    return a


a = [0, 1, 2, 3, 4, 5]
print(cyclic_shift_left(a))
print(cyclic_shift_right(a))

