"""
Вариант 7.
Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации
(л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую
библиотеку питона.  Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.
"""

import tkinter as tk
from tkinter.messagebox import showwarning, showinfo

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

def final():
    control = False
    okay = True
    try:
        stop_num = int(text1.get())
        if stop_num < 2:
            showwarning(title="Ошибка", message="Число должно быть больше 1.")
            okay = False
    except ValueError:
        showwarning(title="Ошибка", message="Введено не число.")
        okay = False

    if okay:
        solution_list = []
        max_solution = 0
        for i_num in range(1, stop_num):
            num_obj = CheckNumber(i_num)
            if num_obj.odd_count == 1:
                if len(str(num_obj.dig_sum)) == 2:
                    dig_obj = CheckNumber(num_obj.dig_sum)
                    if dig_obj.odd_count == 1:
                        control = True
                        formula = num_obj.dig_sum % 7
                        if max_solution == formula:
                            solution_list.append(i_num)
                        if max_solution < formula:
                            max_solution = formula
                            solution_list = [i_num]
        if control:
            newWindow = tk.Toplevel(root)
            newWindow.title('Ответ при n = ' + str(stop_num))
            newWindow.geometry('480x320')
            languages_var = tk.StringVar(value=solution_list)
            listbox = tk.Listbox(newWindow, listvariable=languages_var)
            listbox.pack(side='left', fill='both', expand=1)
            scrollbar = tk.Scrollbar(newWindow, orient="vertical", command=listbox.yview)
            scrollbar.pack(side='right', fill='y')
        else:
            showinfo(title="Ответ", message="Подходящих чисел нет.")


root = tk.Tk()
root.title("Устремленная задача")
root.geometry("720x480")
root.resizable(False, False)

label = tk.Label(text="Данная программа выводит числа до n, с максимальным значением суммы цифр по модулю 7,"
                      "\n в записи которых встречается ровно одна нечетная цифра.\n\
Сумма цифр которых должна быть двузначной, имея ровно одну четную цифру в записи.\n")
label.pack()

label_login = tk.Label(root, text="Введите число n > 1.")
label_login.pack()
text1 = tk.Entry(root, width=30, justify='center')
text1.pack()

btn = tk.Button(text="Вычислить", command=final)
btn.pack(expand=True)

root.mainloop()
