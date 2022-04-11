# В списке, поменять местами самое большое число и самое маленькое число местами
first_list = [1, 3, 12, 74, 7, 16]
min = first_list.index(min(first_list))
max = first_list.index(max(first_list))
print(min)
print(max)
first_list[0],first_list[3]=first_list[3],first_list[0]
print(first_list)
