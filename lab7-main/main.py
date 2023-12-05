"""
Вариант 7.
Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию. 
В программе должны быть реализованы минимум один класс, три атрибута, два метода.

Задание: Вывести все натуральные числа до n, в записи которых встречается ровно одна нечетная цифра.
сумма цифр должна быть двузначной иметь ровно одну четную цифру в записи.
Целевая функция это числа с максимальным значением суммы цифр по модулю 7.
"""

import sys

control = False

odd_num_list = ['1', '3', '5', '7', '9']


class CheckNumber:
    value = None
    odd_count = 0
    dig_sum = 0

    def __init__(self, value):
        self.value = value
        self.odd_check()
        self.digit_check()

    def odd_check(self):
        temp_odd_count = 0
        for check_num in odd_num_list:
            temp_odd_count += str(self.value).count(check_num)
        self.odd_count = temp_odd_count

    def digit_check(self):
        check = 0
        for cypher in str(self.value):
            check += int(cypher)
        self.dig_sum = check


# -------------------Задача---------------------

def final(stop_num):
    solution_list = []
    max_solution = 0
    for i_num in range(1, stop_num):
        num_obj = CheckNumber(i_num)
        if num_obj.odd_count == 1:
            if len(str(num_obj.dig_sum)) == 2:
                dig_obj = CheckNumber(num_obj.dig_sum)
                if dig_obj.odd_count == 1:
                    global control
                    control = True
                    formula = num_obj.dig_sum % 7
                    if max_solution == formula:
                        solution_list.append(i_num)
                    if max_solution < formula:
                        max_solution = formula
                        solution_list = [i_num]
    for i in solution_list:
        print(i, end=' ')


# ----------------------Ввод--------------------
try:
    stop_num = int(input('Введите число n > 1 до которого будут совершены расчёты: '))
    if stop_num < 2:
        sys.exit('Число должно быть больше 1. Программа завершена.')
except ValueError:
    sys.exit('Введено не число. Программа завершена.')

# ---------------------Вывод--------------------

print('Ответ:')
final(stop_num)
if not control:
    print('Подходящих чисел нет')
