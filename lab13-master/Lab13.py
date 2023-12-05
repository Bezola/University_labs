"""
1.Прочитать в виде списков набор данных titanic.csv, взятый из открытых источников
2.Для прочитанного набора выполнить обработку в соответствии со своим вариантом. Библиотекой pandas пользоваться нельзя.

Вариант 7: Определить количество мужчин на борту в возрастном интервале средний возраст +- 15 позиций и сколько из них выжило
"""
import csv

male_list = []

with (open('titanic.csv', 'r') as f):
    csv_reader = csv.reader(f)
    male_count, age_median = 0, 0
    for row in csv_reader:
        if row[3] == 'male':
            male_count += 1
            age_median += float(row[4])
            male_list.append([float(row[4]), int(row[0])])

age_median = int(age_median // male_count)
male_list.sort()

working = True
cursor, answer_list = len(male_list) // 2, [0, 0]
check_direction = 1
while working:
    if male_list[cursor + check_direction][0] in range(age_median - 15, age_median + 16):
        answer_list[0] += 1
        if male_list[cursor + check_direction][1] == 1:
            answer_list[1] += 1
        cursor += check_direction
    elif check_direction == 1:
        check_direction = -1
        cursor -= answer_list[0] - 1
    else:
        break

print(f'Средний возраст мужчин: {age_median}. Всего мужчин в возрастной группе {age_median} +- 15 лет: {answer_list[0]}'
      f'\nИз них выжило: {answer_list[1]}')
