""" Задача №1. Решение в группах
Семинар 1. Ввод-вывод, операторы ветвления
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2

n = int(input())
m = int(input())

print((m + n - 1) // n) """

# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input('Кол-во учащихся в классе a: '))
# b = int(input('Кол-во учащихся в классе b: '))
# c = int(input('Кол-во учащихся в классе c: '))

# s1 = (a + 1) // 2 
# s2 = (b + 1) // 2 
# s3 = (c + 1) // 2 

# print(s1, s2, s3)
# print(s1 + s2 + s3)


""" Задача №5. Решение в группах
Вагоны в электричке пронумерованы натуральными
числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно.
Input: 3 4(ввод на разных строках)
Output: 6
"""

# i = int(input('i = '))
# j = int(input('j = '))
# if i == j:
#   print('Нужна доп. инфа')
# else: 
#   print(i + j - 1)


""" Задача №7. Решение в группах
Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400. 
Input: 2016
Output: YES """

# year = int(input('Введите год - '))

# if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
#   print('YES')
# else:
#   print('NO')

# list_1 = [1, 5]
# list_1.append(10) # append добавляет значение в конец массива
# list_1.append(85)
# print(list_1)


# list_1 = []
# print(list_1)
# for i in range(5):
#   list_1.append(i)
#   print(list_1)

# list.append() - добавление нового элемента в список в конец
# list.pop() - удаление последнего элемента списка, так же pop возвращает значение. Если в аргумент pop() указать какое-либо значение, то это значение станет индексом удаляемого элемента
""" list_1 = [1, -2, 20, 7]
print(list_1)
a = list_1.pop(0)
print(a)
print(list_1.pop())
print(list_1.pop(1)) """

# Добавление элемента в список на какую-либо позицию. insert

""" list_1 = [1, 2, 3, 4, 5]

list_1.insert(2, 21)
print(list_1) """

"""list_1 = [1, 2, 3, 4, 5]
print(list_1[:]) - [1, 2, 3, 4, 5] 
Если перед двоеточиями ничего нет, то значит начинается с начала списка, если после нет, то завершаем в конце, т.е. выводим весть список полностью
print(list_1[:2]) [1, 2] 
print(list_1[1:4]) [3, 5] 
""" 


# a = 0
# flag = True
# while flag: 
# 	print(a)
# 	a += 1
# 	if a == 5:
# 		flag = False


# for i in range(15, 3, -1): # range, цикл выполняется столько раз, смотря какое значение у range, если for i in range(5): print(i), то будет от 0 до 4, не включая значение в range. В range 3 значения, range(1, 10, 3) 1 - с какого числа начинается, с единицы, потом до какого числа - 10, и с шагом 3. - 1, 4, 7
  # print(i)
  

# print(range(5)) // range(0, 5)
# Если вывести просто range(5), то ничего не будет, выведется просто range(0, 5), но если преобразовать range в список, list, то 
# print(list(range(5))) # [0, 1, 2, 3, 4]
# По сути range создаёт последовательность из чисел 0-4, и вот как раз отсюда i наша и принимает значения.
# for i in range(5):
#   print(i)

""" По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5 = 5! = 1 * 2 * 3* 4 * 5 = 120
Output: 120
"""
# Первое решение, в 2 переменных
a = int(input("Введите число: "))
result = 1 
# Решение в 2 переменные
while a > 0:
  result *= a # 1 * 5 = 5, 5 * 4 = 20, 20 * 3 = 120
  a -= 1
print(result)

# while i <= a: 
#   result *= i 
#   i += 1
# print("Факториал числа", a, "=", result)
