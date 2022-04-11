# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
name = input('Введите имя')
email = input('Введите email')
sl1 = dict(name=name, email=email) #первый словарь
print(sl1)
n = int(input('Введите n'))
lst1 = list(range(0, n+1)) #ключи для 2-го словаря
print(lst1)
sl2 = dict(lst1=sl1) #2 словарь
print(sl2)
