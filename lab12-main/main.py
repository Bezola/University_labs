"""Вычислить сумму знакопеременного ряда |х(3n-1)|/(3n-1)!, где х-матрица ранга к (к и матрица задаются
случайным образом), n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков
после запятой. У алгоритма д.б. линейная сложность. Операция умножения –поэлементная. Знак первого слагаемого  +."""

import random
import numpy as np
from decimal import Decimal, getcontext


def fractional_part_len(number_to_count):  # Подсчёт кол-ва знаков после запятой
    return Decimal(number_to_count).as_tuple().exponent * (-1)


int_t = input('Введите число t >= 1 (кол-во знаков после запятой до которых будет совершен рассчёт): ')  # Ввод и проверка введёного числа t
while True:
    try:
        int_t = int(int_t)
    except ValueError:
        print('Ошибка: введено не число. Повторите ввод.')
        int_t = None
    finally:
        if int_t is None:
            pass
        elif int_t < 1:
            print('Ошибка: число меньше еденицы. Повторите ввод.')
        else:
            getcontext().prec = int_t  # Присвоение глубины Decimal
            break
    int_t = input('Введите число t >= 1:')

int_k = random.randint(1, 10)  # Cоздание и вывод матрицы
matrix_x = np.random.uniform(-1.0, 1.0, (int_k, int_k))
print('Матрица x:\n' + str(matrix_x))

dict_initials = {"n": 1, "calculated_matrix": matrix_x,
                 "factorial_divisor": None, "current_answer": 0}  # Исходники вычислений

# Вычисление суммы знакопеременного ряда
while fractional_part_len(dict_initials["current_answer"]) < int_t:  # Вычисления до t знаков после запятой
    int_current_operator = dict_initials["n"] * 3 - 1

    if int_current_operator == 2:
        dict_initials["calculated_matrix"] *= matrix_x  # Ход 1: Умножение матриц (возведение в степень)
        dict_initials["factorial_divisor"] = 2  # Ход 1: Вычисление факториала
    else:
        dict_initials["calculated_matrix"] *= (matrix_x ** 3)  # Ход n: Умножение матриц (возведение в степень)
        for j in [0, 1, 2]:  # Ход n: Вычисление факториала
            dict_initials["factorial_divisor"] = dict_initials["factorial_divisor"] * (int_current_operator - j)

    # Вычисление слагаемого и добавление к ответу
    if dict_initials["n"] % 2 == 1:
        dict_initials["current_answer"] += \
            Decimal(np.linalg.det(dict_initials["calculated_matrix"])) / Decimal(dict_initials["factorial_divisor"])
    else:
        dict_initials["current_answer"] -= \
            Decimal(np.linalg.det(dict_initials["calculated_matrix"])) / Decimal(dict_initials["factorial_divisor"])

    dict_initials["n"] += 1  # Вычисление следующего числа

print('Ответ: ' + str(dict_initials["current_answer"]))
