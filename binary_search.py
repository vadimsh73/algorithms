# -*-coding:UTF-8-*-

# Алгоритм бинарного поиска в отсортированном списке


def binary_search(my_list, item):
    """
    :param my_list: A sorted list of numbers (Отсортированный список чисел)
    :param item: The value of the index which you want to find
    (Искомое значение)
    :return:the index of the found value , if there is no such value then none
     (индекс найденого значения , если такого значения нет то none)
    """

    low = 0  # Минимальная граница списка в которой выполняется поиск
    high = len(my_list) - 1  # Максимальная граница списка

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


