# -*-coding:UTF-8-*-


def invert_array(A):
    """
    Обращение массива(поворот задом наперед)
    в рамках индекса от 0 до len(n)-1
    :param A: list
    :return:
    """

    for i in range(len(A)//2):
        A[i], A[len(A)-1 - i] = A[len(A)-1 - i], A[i]
    return A


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    A1 = invert_array(A1)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")
    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    A2 = invert_array(A2)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")


test_invert_array()