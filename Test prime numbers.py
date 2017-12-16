# -*-coding:UTF-8-*-


def is_simple_number(x):
    """
    Определяет является ли число простым
    Если простое то возвращает True, а иначе - False
    :param x: Целое положительное число
    :return: True or False
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def factorize_number(x):
    """
    Расскладывает число на множители
    печатает их на экран
    :param x:Целое положительное
    :return: Печатает множители числа x
    """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor +=1
x = int(input("X = "))
print(is_simple_number(x))
factorize_number(x)