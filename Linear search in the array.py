# -*-coding:UTF-8-*-


def array_search(a:list, n:int, x:int):
    """
    Осуществляет поиск числа x в масстве A
    от 0 до N-1 включительно.
    :param a: type list
    :param n: type int
    :param x: type int
    :return: Возвращает индекс элемента x в массиве A
             или -1 если такого элемента нет
             если в массиве несколько одинаковых элементов
             то вернуть индекс первого из них
    """
    for i in range(n):
        if a[k] == x:
            return k

    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")
    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

test_array_search()