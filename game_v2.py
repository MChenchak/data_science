"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def recursive_predict(low: int, hight: int, number: int = 1) -> int:
    """Рекурсивный поиск числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        low (int, mandatory): Нижняя граница поиска.
        hight (int, mandatory): Верхняя граница поиска.

    Returns:
        int: Число попыток
    """

    mid = (low + hight) // 2

    if mid == number:
        return 1

    if mid > number:
        return 1 + recursive_predict(low, mid - 1, number)

    elif mid < number:
        return 1 + recursive_predict(mid + 1, hight, number)


def score_game(predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        recursive_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(recursive_predict(0, 100, number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(recursive_predict)
