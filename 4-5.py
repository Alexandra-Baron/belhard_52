# Дан список чисел, сказать сколько чисел в нем повторяется
first_list = [1, 3, 4, 5, 5, 7, 7, 9, 9, 2, 7, 7]
number_list = len(first_list) #количество эл-в в списке
set_1 = set(first_list)
unique = set.difference(set_1) #уникальные значения
number_set = len(unique) #кол-во уникальных значений
final = number_list-number_set
print(final)
