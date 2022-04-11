#Даны два списка чисел, найти сумму общих элементов (без дублей) этих списков
first_list = [1, 3, 5, 8]
second_list = [3, 4, 6, 8]
set_1 = set(first_list)
set_2 = set(second_list)
result = sum(set.intersection(set_1,set_2))
print(result)
